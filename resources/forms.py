from django import forms

from .models import Resource, Feedback, Photo

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('title', 'description', 'difficult_education', 'difficult_student', 'value', 'url', 'tags', 'languages', 'resources')
        labels = {
            "title": "Título:",
            "description": "Descrição:",
            "difficult_education": "Dificuldade para o educador:",
            "difficult_student": "Dificuldade para o estudante:",
            "value": "Valor (se houver):",
            "url": "Link para acessar o recurso (se houver):",
            "tags": "Tags:",
            "languages": "Idiomas:",
            "resources": "Recursos relacionados:"
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('title', 'description', 'is_pro')

class FeedbackAnonymousForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('anonymous', 'title', 'description', 'is_pro')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        labels = { 'image': 'Imagem'}
