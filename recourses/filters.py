from .models import Recourse
import django_filters

class RecourseFilter(django_filters.FilterSet):
    class Meta:
        model = Recourse
        fields = ['difficult_education', 'difficult_student', 'title', 'value',  ]
