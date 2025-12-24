from django.contrib import admin
from .models import Article, Comment

# Register Article Model
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')

# Register Comment Model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'author', 'article')

