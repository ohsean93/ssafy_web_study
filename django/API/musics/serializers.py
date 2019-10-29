from rest_framework import serializers
from .models import Music, Artist, Comment


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('pk', 'title', 'artist_id',)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('pk', 'name',)


class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)

    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('music_set',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id',)


class MusicDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comment_set',)
