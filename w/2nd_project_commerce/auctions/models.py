from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, TextField, DecimalField, BooleanField, ForeignKey, CASCADE


class User(AbstractUser):
    pass


class Listing(Model):
    title = CharField(max_length=64)
    description = TextField(max_length=2048)
    image = ImageField(max_length = 200, null=True, blank=True, upload_to="media")

    price = DecimalField(max_digits=6, decimal_places=2)
    seller = ForeignKey(User, on_delete=CASCADE, related_name='listings')
    active = BooleanField(default=True)

    category_choices = [
        ('Mo', 'Motors'),
        ('Fa', 'Fashion'),
        ('Ho', 'Home Garden'),
        ('Co', 'Collectables & Art'),
        ('El', 'Electronics'),
        ('Sp', 'Sports, Hobbies & Leisure'),
        ('He', 'Health & Beauty'),
        ('Me', 'Media'),
        ('Bu', 'Business, Office & Industrial Supplies'),
        ('Ot', 'Others')
    ]
    category = CharField(max_length=2, choices=category_choices, null=True, blank=True)

    def __str__(self):
        return self.title


class Bidding(Model):
    listing = ForeignKey(Listing, on_delete=CASCADE, related_name='biddings')
    bidder = ForeignKey(User, on_delete=CASCADE, related_name='biddings')
    price = DecimalField(max_digits=6, decimal_places=2)


class Comment(Model):
    listing = ForeignKey(Listing, on_delete=CASCADE, related_name='comments')
    commenter = ForeignKey(User, on_delete=CASCADE, related_name='comments')
    comment = TextField(max_length=2048)
