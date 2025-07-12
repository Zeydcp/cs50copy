from django.contrib.auth.models import AbstractUser
from django.db.models import Model, TextField, ForeignKey, DateTimeField, CASCADE


class User(AbstractUser):
    def follower_count(self):
        return self.followers.count()

    def following_count(self):
        return self.follows.count()

    @property
    def posts_liked(self):
        return Like.objects.filter(liker=self).values_list("post_id", flat=True)


class Post(Model):
    body = TextField(max_length=2048)
    posted_by = ForeignKey(User, on_delete=CASCADE, related_name="posts")
    timestamp = DateTimeField(auto_now=True)

    def like_count(self):
        return self.likes.count()


class Like(Model):
    liker = ForeignKey(User, on_delete=CASCADE, related_name="likes")
    post = ForeignKey(Post, on_delete=CASCADE, related_name="likes")
    timestamp = DateTimeField(auto_now=True)


class Comment(Model):
    comment = TextField(max_length=2048)
    commenter = ForeignKey(User, on_delete=CASCADE, related_name="comments")
    post = ForeignKey(Post, on_delete=CASCADE, related_name="comments")
    timestamp = DateTimeField(auto_now=True)


class Follow(Model):
    user_1 = ForeignKey(User, on_delete=CASCADE, related_name="follows")
    user_2 = ForeignKey(User, on_delete=CASCADE, related_name="followers")
    timestamp = DateTimeField(auto_now=True)
