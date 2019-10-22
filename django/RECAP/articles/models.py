from django.db import models
from django.urls import reverse
from django.contrib import auth
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-pk',)

    #method도 추가 예정
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk': self.pk})


class Comment(models.Model):
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # article = models.ForeignKey(Article, on_delete='CASCADE')

    def __str__(self):
        return self.content

    #method도 추가 예정
    def get_absolute_url(self):
        return reverse('articles:update_comment', kwargs={'article_pk': self.article.pk, 'comment_pk': self.pk})


