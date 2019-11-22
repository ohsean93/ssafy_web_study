from django.shortcuts import render, get_object_or_404
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer, MovieDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
# from

# Create your views here.
@api_view(['GET'])
def movie_index(request):
    movies = Movie.objects.all()
    
    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
    return Response(status=405)
 

@api_view(['GET', 'POST',])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie_id=movie_pk, user_id=request.user.id)
            if request.user.is_superuser:
                return Response({'massage': '관리자 권한으로 작성되었습니다.'})
            else:
                return Response({'massage': '작성되었습니다.'})


@api_view(['PUT', 'DELETE',])
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if review.movie_id == movie_pk:
            if serializer.is_valid():
                serializer.save()
                return Response({'massage': '수정되었습니다.'}) 
        else:
            return Response({'status':405, 'massage': '잘못된 접근입니다.'})

    elif request.method == 'DELETE':
        review.delete()
        return Response({'massage': '삭제되었습니다.'})
    
    return Response(status=405)


'''
@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializers(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)


@api_view(['GET'])
def user_detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    if request.user != user:
        return Response(status=404)

    serializer = UserSerializers(user)
    return Response(serializer.data)
'''