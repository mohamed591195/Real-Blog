from django.contrib import admin
from .models import Author, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'user', 'sex']
    
admin.site.register(Author)