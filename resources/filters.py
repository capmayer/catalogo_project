from .models import Resource
import django_filters

class ResourceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Resource
        fields = {
            'difficult_education':['exact'],
            'difficult_student':['exact'],
            'languages':['exact'],
        }
        labels = {
            "difficult_education": "Dificuldade para o educador:",
            "difficult_student": "Dificuldade para o estudante:",
            "languages": "Linguas:"
        }
