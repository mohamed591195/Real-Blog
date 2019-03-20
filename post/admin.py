from django.contrib import admin
from .models import Post, Comment, CommentReply

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', ]
    date_hierarchy = 'published'
    list_filter = ['status', 'author']
    search_fields = ['title', 'body']
