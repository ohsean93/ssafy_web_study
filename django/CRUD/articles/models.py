from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img_url = models.TextField()

    def __str__(self):
        return f'{self.id} : {self.title}'