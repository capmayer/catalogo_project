from .models import Resource
import django_filters

class ResourceFilter(django_filters.FilterSet):
    class Meta:
        model = Resource
        fields = {
            'difficult_education':['exact'],
            'difficult_student':['exact'],
            'title':['exact', 'icontains']
        }
        labels = {
            "difficult_education": "Dificuldade para o educador:",
            "difficult_student": "Dificuldade para o estudante:",
            "title": "Nome: ",
        }
