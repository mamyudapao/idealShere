from django.contrib import admin

from posts.models import Post, Comment, Member, Notification, Chat

class IdDisplayAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(Post, IdDisplayAdmin)
admin.site.register(Comment, IdDisplayAdmin)
admin.site.register(Member, IdDisplayAdmin)
admin.site.register(Notification, IdDisplayAdmin)
admin.site.register(Chat, IdDisplayAdmin)