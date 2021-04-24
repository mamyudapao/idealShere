from django.db import models
from django.core import validators
from idealShere.settings import AUTH_USER_MODEL

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=240)
    invitation = models.BooleanField()
    member_number = models.IntegerField(validators=[validators.MinValueValidator(0),
                                                    validators.MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(AUTH_USER_MODEL)
    image = models.ImageField(upload_to='api/posts', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    content = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    voters = models.ManyToManyField(AUTH_USER_MODEL, related_name="likes_user")

    def __str__(self):
        return self.content

class Chat(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=240)
    room = models.ForeignKey('posts.Post', on_delete=models.CASCADE)

class Member(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='member')
    post = models.ForeignKey(
        'posts.Post', on_delete=models.CASCADE, related_name='post_project')
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    sender_id = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    post_id = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
