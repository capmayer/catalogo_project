from django.shortcuts import render
from .models import Recourse, Pro, Con, Feedback
from .filters import RecourseFilter


def home(request):
    recourses_list = Recourse.objects.all()
    return render(request, 'recourses/home.html', { 'recourses_list': recourses_list })

def recourses_list(request):
    recourses_list = Recourse.objects.all()
    recourse_filter = RecourseFilter(request.GET, queryset=recourses_list)
    return render(request, 'recourses/recourse_list.html', { 'recourse_filter': recourse_filter })

def recourse_detail(request, slug):
    recourse = Recourse.objects.get(slug=slug)
    feedback_list = Feedback.objects.filter(recourse=recourse)
    pro_list = Pro.objects.filter(recourse=recourse)
    con_list = Con.objects.filter(recourse=recourse)
    return render(request, 'recourses/recourse_detail.html', { 'recourse': recourse, 'feedback_list': feedback_list, 'pro_list': pro_list, 'con_list': con_list })
