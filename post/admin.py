from django.contrib import admin
from .models import Post, Comment, CommentReply, Author, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', ]
    date_hierarchy = 'published'
    list_filter = ['status', 'author']
    search_fields = ['title', 'body']
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'user', 'sex']
    
admin.site.register(Author)