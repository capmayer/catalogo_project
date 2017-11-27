from rest_framework import serializers

from .models import Resource, Feedback, Image, Like, Deslike

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'is_main', 'resource')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('author', 'created_date')

class DeslikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deslike
        fields = ('author', 'created_date')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('uuid', 'resource', 'title', 'description', 'likes', 'deslikes', 'created_date', 'author')


class ResourceSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(many=True)
    feedback_set = FeedbackSerializer(many=True)
    class Meta:
        model = Resource
        fields = ('title', 'description', 'slug', 'languages', 'url', 'image_set', 'feedback_set', 'likes', 'deslikes', 'difficult_student')
