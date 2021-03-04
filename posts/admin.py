from django.contrib import admin

from posts.models import Post, Comment, Member, Like
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Member)
admin.site.register(Like)