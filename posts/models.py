from django.db import models
from django.core import validators
from idealShere.settings import AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=240)
    category = models.CharField(max_length=100)
    invitation = models.BooleanField()
    member_number = models.IntegerField(validators=[validators.MinValueValidator(0),
                                                    validators.MaxValueValidator(10)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_id = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    content = models.CharField(max_length=240)

    def __str__(self):
        return self.content