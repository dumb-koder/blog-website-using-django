from django.contrib import admin
from .models import Post, Category, Comment

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('pub_date', 'author', 'categories')
    search_fields = ('title', 'content')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'pub_date')
    list_filter = ('post', 'pub_date')
    search_fields = ('author', 'content')
    
