from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    list_display_links = ('pk', 'title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at', 'article')
    list_display_links = ('pk', 'content')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

