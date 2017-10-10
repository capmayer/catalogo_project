from django import forms
from .models import Resource, Feedback, Image, Tag

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('title', 'description', 'difficult_education', 'difficult_student', 'url', 'tags')
        labels = {
            "title": "Título:",
            "description": "Descrição:",
            "difficult_education": "Dificuldade para o educador:",
            "difficult_student": "Dificuldade para o estudante:",
            "url": "Link para acessar o recurso:",
            "tags": "Tags:"
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('title', 'description')
        labels = {
            'title': 'Título',
            'description': 'Descrição'
        }

class FeedbackAnonymousForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('anonymous', 'title', 'description')
        labels = {
            'anonymous': 'Nome',
            'title': 'Título',
            'description': 'Descrição'
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
        labels = {
            'name': 'Tag'
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        labels = { 'image': 'Imagem: '}
