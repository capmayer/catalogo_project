from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Resource, Feedback, Photo
from .filters import ResourceFilter
from .forms import ResourceForm, FeedbackForm, FeedbackAnonymousForm, PhotoForm


def home(request):
    resources_list = Resource.objects.filter(photo__is_main=True)
    photos_list = Photo.objects.filter(resource__in=resources_list)
    general_list = zip(resources_list, photos_list)
    return render(request, 'resources/home.html', { 'general_list': general_list })

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
        try:
            image = Photo.objects.get(resource=resource, is_main=True)
        except:
            image = None
        if request.user.is_authenticated:
            feedback_form = FeedbackForm()
        else:
            feedback_form = FeedbackAnonymousForm()
        return render(request, 'resources/resource_detail.html', { 'resource': resource, 'pro_list': pro_list, 'con_list': con_list, 'feedback_form': feedback_form, 'image': image })

def resource_new(request):
    if request.method == "POST":
        resource_form = ResourceForm(request.POST)
        image_form = PhotoForm(request.POST, request.FILES)
        if resource_form.is_valid() and image_form.is_valid():
            resource = resource_form.save(commit=False)

            if request.user.is_authenticated:
                resource.author = request.user

            resource.save()

            image = image_form.save(commit=False)

            image.resource = resource
            image.is_main = True

            image.save()

            return redirect('resource_detail', slug=resource.slug)
        else:
            print(image_form.errors)
    else:
        resource_form = ResourceForm()
        image_form = PhotoForm()
    return render(request, 'resources/resource_new.html', { 'resource_form': resource_form, 'image_form':image_form })
