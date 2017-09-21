from django.shortcuts import render, redirect
from .models import Recourse, Pro, Con, Feedback
from .filters import RecourseFilter
from .forms import RecourseForm, FeedbackForm, FeedbackAnonymousForm


def home(request):
    recourses_list = Recourse.objects.all()
    return render(request, 'recourses/home.html', { 'recourses_list': recourses_list })

def recourses_list(request):
    recourses_list = Recourse.objects.all()
    recourse_filter = RecourseFilter(request.GET, queryset=recourses_list)
    return render(request, 'recourses/recourse_list.html', { 'recourse_filter': recourse_filter })

def recourse_detail(request, slug):
    recourse = Recourse.objects.get(slug=slug)
    if request.method == "POST":
        if request.user.is_authenticated:
            form = FeedbackForm(request.POST)
        else:
            form = FeedbackAnonymousForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            if request.user.is_authenticated:
                feedback.author = request.user
            feedback.recourse = recourse
            feedback.save()
            return redirect('recourse_detail', slug=slug)
    else:
        feedback_list = Feedback.objects.filter(recourse=recourse)
        pro_list = Pro.objects.filter(recourse=recourse)
        con_list = Con.objects.filter(recourse=recourse)
        if request.user.is_authenticated:
            feedback_form = FeedbackForm()
        else:
            feedback_form = FeedbackAnonymousForm()
        return render(request, 'recourses/recourse_detail.html', { 'recourse': recourse, 'feedback_list': feedback_list, 'pro_list': pro_list, 'con_list': con_list, 'feedback_form': feedback_form })

def recourse_new(request):
    if request.method == "POST":
        form = RecourseForm(request.POST)
        if form.is_valid():
            recourse = form.save(commit=False)
            if request.user.is_authenticated:
                recourse.author = request.user
            recourse.save()
            return redirect('recourse_detail', slug=recourse.slug)
    else:
        form = RecourseForm()
    return render(request, 'recourses/recourse_new.html', { 'form': form})
