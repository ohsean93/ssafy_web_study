from rest_framework import serializers
from .models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'audience', 'poster_url', 'description', 'genres')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('pk', 'content', 'score', 'user_id', 'movie_id')


class MovieDetailSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = MovieSerializer.Meta.fields + ('review_set',)


# 모델모델
'''
class Genre(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'movie_pk': self.pk})

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-pk',)


class Review(models.Model):
    content = models.TextField()
    score = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
'''