from .models import Resource
import django_filters

class ResourceFilter(django_filters.FilterSet):
    class Meta:
        model = Resource
        fields = ['difficult_education', 'difficult_student',]
        labels = {
            "difficult_education": "Dificuldade para o educador:",
            "difficult_student": "Dificuldade para o estudante:",
        }
