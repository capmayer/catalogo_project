from django.shortcuts import render
from .models import Recourse

# Create your views here.
def home(request):
    recouses_list = Recourse.objects.all()
    return render(request, 'recourses/home.html', { 'recourses_list': recouses_list })

def recourse_detail(request, slug):
    recourse = Recourse.objects.get(slug=slug)
    return render(request, 'recourses/recourse_detail.html', { 'recourse': recourse })
