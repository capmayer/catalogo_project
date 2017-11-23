import json, boto3

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import modelformset_factory

from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from .models import Resource, Feedback, Image
from .filters import ResourceFilter
from .forms import ResourceForm, FeedbackForm, FeedbackAnonymousForm, ImageForm, TagForm


def home(request):
    resources_list = Resource.objects.filter(image__is_main=True).order_by("-created_date")
    return render(request, 'resources/home.html', { 'resources_list': resources_list })

def resources_list(request):
    resources_list = Resource.objects.filter(image__is_main=True)
    resource_filter = ResourceFilter(request.GET, queryset=resources_list)
    return render(request, 'resources/resource_list.html', { 'resource_filter': resource_filter })

def resource_detail(request, slug):
    # get the specified resource
    resource = Resource.objects.get(slug=slug)

    # count the views of a resource
    hit_count = HitCount.objects.get_for_object(resource)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    # check method
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
            if 'good_feedback' in request.POST:
                feedback.is_pro = True
            elif 'bad_feedback' in request.POST:
                feedback.is_pro = False

            feedback.save()
            return redirect('resource_detail', slug=slug)
    else:
        pro_list = Feedback.objects.filter(resource=resource, is_pro=True)
        con_list = Feedback.objects.filter(resource=resource, is_pro=False)
        try:
            image = Image.objects.get(resource=resource)
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
        image_form = ImageForm(request.POST, request.FILES)
        tag_form = TagForm(request.POST)
        if 'tag_submit' in request.POST:
            if tag_form.is_valid():
                tag = tag_form.save()
        else:
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
        resource_form = ResourceForm()
        image_form = ImageForm()
        tag_form = TagForm()
    return render(request, 'resources/resource_new.html', { 'resource_form': resource_form, 'image_form': image_form, 'tag_form': tag_form })

def resource_all(request):
    resources = serialize("json", Resource.objects.filter(image__is_main=True))
    return HttpResponse(resources, content_type="application/json")
