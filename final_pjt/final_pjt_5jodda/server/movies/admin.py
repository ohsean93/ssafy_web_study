from django.contrib import admin
from .models import Movie, Genre, Review

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    # admin에서 무엇을 볼 지 지정
    list_display = ('title', 'audience', 'poster_url', 'description', )
    filter_horizontal = ('genres',)
    list_display_links = ['title',]
    

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content', 'score', )
    list_display_links = ['content',]


class GenreAdmin(admin.ModelAdmin):
    list_display =  ('name', )

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Genre, GenreAdmin)