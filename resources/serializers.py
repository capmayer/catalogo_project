from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from django.contrib.auth.models import User
from .models import Resource, Feedback, Image, Like, Deslike, Relato


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

class ResourceSimpleSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(many=True)
    class Meta:
        model = Resource
        fields = ('image_set', )

class ResourceSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(many=True)
    feedback_count = serializers.IntegerField(source='feedback_set.count', read_only=True)
    relato_count = serializers.IntegerField(source='relato_set.count', read_only=True)
    visualization_count = serializers.IntegerField(source='hit_count_generic.count', read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    deslikes_count = serializers.IntegerField(source='deslikes.count', read_only=True)
    resources = ResourceSimpleSerializer(many=True)
    class Meta:
        model = Resource
        fields = ('id','title', 'description', 'slug', 'languages', 'url', 'image_set', 'feedback_count', 'likes_count', 'deslikes_count', 'difficult_student', 'visualization_count',
        'relato_count', 'resources')
        depth = 2


class FeedbackSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    deslikes_count = serializers.IntegerField(source='deslikes.count', read_only=True)
    class Meta:
        model = Feedback
        fields = ('uuid', 'resource', 'description', 'likes_count', 'deslikes_count', 'created_date', 'author', 'is_pro')

class RelatoSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    deslikes_count = serializers.IntegerField(source='deslikes.count', read_only=True)
    class Meta:
        model = Relato
        fields = ('uuid', 'resource', 'description', 'likes_count', 'deslikes_count', 'created_date', 'author')
