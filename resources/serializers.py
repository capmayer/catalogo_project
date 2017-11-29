from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Resource, Feedback, Image, Like, Deslike


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'is_main', 'resource',)

class LikeSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Like
        fields = ('author', 'created_date',)

class DeslikeSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Deslike
        fields = ('author', 'created_date',)

class ResourceSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(many=True)
    feedback_count = serializers.IntegerField(source='feedback_set.count', read_only=True)
    visualization_count = serializers.IntegerField(source='hit_count_generic.count', read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    deslikes_count = serializers.IntegerField(source='deslikes.count', read_only=True)
    class Meta:
        model = Resource
        fields = ('id','title', 'description', 'slug', 'languages', 'url', 'image_set', 'feedback_count', 'likes_count', 'deslikes_count', 'difficult_student', 'visualization_count')


class FeedbackSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    deslikes_count = serializers.IntegerField(source='deslikes.count', read_only=True)
    class Meta:
        model = Feedback
        fields = ('uuid', 'resource', 'title', 'description', 'likes_count', 'deslikes_count', 'created_date', 'author', 'anonymous', )
