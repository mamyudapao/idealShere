from django.db import models
from django.core import validators
from idealShere.settings import AUTH_USER_MODEL

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=240)
    category = models.CharField(max_length=100)
    invitation = models.BooleanField()
    member_number = models.IntegerField(validators=[validators.MinValueValidator(0),
                                                    validators.MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='api/posts', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    content = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Like(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    comment = models.ForeignKey('posts.Comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'comment']


class Member(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='member')
    post = models.ForeignKey(
        'posts.Post', on_delete=models.CASCADE, related_name='post_project')
    created_at = models.DateTimeField(auto_now_add=True)
