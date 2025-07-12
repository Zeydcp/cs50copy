from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ForeignKey, TextField, IntegerField, CASCADE, URLField, Sum, Count, F, ExpressionWrapper, FloatField, BooleanField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm, Textarea, RadioSelect


class User(AbstractUser):
    @property
    def reviews_liked(self):
        return Like.objects.filter(liker=self).values_list("review_id", flat=True)


class Restaurant(Model):
    place_id = CharField(max_length=100, primary_key=True)
    name = CharField(max_length=255)
    photo_url = URLField(blank=True, null=True)  # stores a usable photo URL

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        annotated_reviews = self.reviews.annotate(
            like_count=Count('likes'),
            weight=ExpressionWrapper(F('like_count') + 1, output_field=FloatField()),
            weighted_rating=ExpressionWrapper(
                F('rating') * (F('like_count') + 1), output_field=FloatField())
        )

        aggregated = annotated_reviews.aggregate(
            total_weight=Sum('weight'),
            total_weighted_rating=Sum('weighted_rating')
        )

        total_weight = aggregated['total_weight']
        total_weighted_rating = aggregated['total_weighted_rating']

        return round(total_weighted_rating / total_weight) if total_weight else None

    def serialize(self):
        return {
            "id": self.place_id,
            "name": self.name,
            "image": self.photo_url,
            "rating": self.average_rating
        }


class Review(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    place = ForeignKey(Restaurant, on_delete=CASCADE, related_name='reviews')
    review = TextField()
    rating = IntegerField(default=0, validators=[
                          MinValueValidator(0), MaxValueValidator(4)], blank=True)
    edited = BooleanField(default=False)

    def __str__(self):
        return f'Review by {self.user.username} on {self.place.name}'

    @property
    def like_count(self):
        return self.likes.count()

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "restaurant_rating": self.place.average_rating,
            "restaurant_id": self.place.place_id,
            "review": self.review,
            "rating": self.rating,
            "count": self.like_count,
            "edited": self.edited
        }


class Like(Model):
    liker = ForeignKey(User, on_delete=CASCADE, related_name="likes")
    review = ForeignKey(Review, on_delete=CASCADE, related_name="likes")


class NewReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating']

        widgets = {
            'review': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your review here...',
                'rows': 3,
                'style': 'max-width: 30%;',
            }),
            'rating': RadioSelect(choices=[(i, f'{i} Stars') for i in range(1, 5)])
        }
        labels = {
            'review': 'Review',
            'rating': 'Rating (0–4)'
        }
