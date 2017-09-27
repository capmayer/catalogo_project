from django import forms

from .models import Resource, Feedback

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('title', 'description', 'difficult_education', 'difficult_student', 'value', 'url', 'tags', 'languages', 'resources')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('title', 'description', 'is_pro')

class FeedbackAnonymousForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('anonymous', 'title', 'description', 'is_pro')
