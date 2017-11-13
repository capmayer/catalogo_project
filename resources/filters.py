from .models import Resource
import django_filters

class ResourceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    ordering = django_filters.OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('created_date', 'Data de Criação'),

        )
    )

    class Meta:
        model = Resource
        fields = {
            'difficult_education':['exact'],
            'difficult_student':['exact'],
            'languages':['exact'], 'ordering':['exact'],
        }
        labels = {
            "difficult_education": "Dificuldade para o educador:",
            "difficult_student": "Dificuldade para o estudante:",
            "languages": "Linguas:"
        }
