from django.shortcuts import render, redirect
from .models import Resource, Feedback
from .filters import ResourceFilter
from .forms import ResourceForm, FeedbackForm, FeedbackAnonymousForm


def home(request):
    resources_list = Resource.objects.all()
    return render(request, 'resources/home.html', { 'resources_list': resources_list })

def resources_list(request):
    resources_list = Resource.objects.all()
    resource_filter = ResourceFilter(request.GET, queryset=resources_list)
    return render(request, 'resources/resource_list.html', { 'resource_filter': resource_filter })

def resource_detail(request, slug):
    resource = Resource.objects.get(slug=slug)
    if request.method == "POST":
        if request.user.is_authenticated:
            form = FeedbackForm(request.POST)
        else:
            form = FeedbackAnonymousForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            if request.user.is_authenticated:
                feedback.author = request.user
            feedback.resource = resource
            feedback.save()
            return redirect('resource_detail', slug=slug)
    else:
        pro_list = Feedback.objects.filter(resource=resource, is_pro=True)
        con_list = Feedback.objects.filter(resource=resource, is_pro=False)
        if request.user.is_authenticated:
            feedback_form = FeedbackForm()
        else:
            feedback_form = FeedbackAnonymousForm()
        return render(request, 'resources/resource_detail.html', { 'resource': resource, 'pro_list': pro_list, 'con_list': con_list, 'feedback_form': feedback_form })

def resource_new(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            if request.user.is_authenticated:
                resource.author = request.user
            resource.save()
            return redirect('resource_detail', slug=resource.slug)
    else:
        form = ResourceForm()
    return render(request, 'resources/resource_new.html', { 'form': form})
