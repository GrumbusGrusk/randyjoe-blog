from django.contrib import admin
from .models import Post, Comment, Albums, Music

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Albums)
admin.site.register(Music)
