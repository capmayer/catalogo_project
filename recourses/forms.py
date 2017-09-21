from django import forms

from .models import Recourse, Feedback

class RecourseForm(forms.ModelForm):
    class Meta:
        model = Recourse
        fields = ('title', 'description', 'difficult_education', 'difficult_student', 'value', 'url', 'tags', 'languages', 'recourses')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('title', 'description')

class FeedbackAnonymousForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('anonymous', 'title', 'description')
