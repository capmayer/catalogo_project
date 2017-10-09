from django import forms
from .models import Resource, Feedback, Image

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
        fields = ('title', 'description')

class FeedbackAnonymousForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('anonymous', 'title', 'description')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        labels = { 'image': 'Imagem'}
