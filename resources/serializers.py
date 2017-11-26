from rest_framework import serializers

from .models import Resource, Feedback, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'is_main', 'resource')

class ResourceSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(many=True)
        
    class Meta:
        model = Resource
        fields = ('title', 'description', 'slug', 'languages', 'url', 'resources', 'image_set', 'difficult_student')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('uuid', 'resource', 'title', 'description', 'good_avaliations', 'bad_avaliations')
