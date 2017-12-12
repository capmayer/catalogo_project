import json, boto3

from django.core.serializers import serialize
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from .models import Resource, Feedback, Image, Relato
from .filters import ResourceFilter
from .serializers import ResourceSerializer, FeedbackSerializer, LikeSerializer, DeslikeSerializer, RelatoSerializer

def home(request):
    return render(request, 'resources/home.html', { 'userName': request.user.username, 'userId': request.user.id })

def resources_list(request):
    return render(request, 'resources/resource_list.html', { 'userName': request.user.username, 'userId': request.user.id })

@ensure_csrf_cookie
def resource_detail(request, slug):
    return render(request, 'resources/resource_detail.html', { 'userName': request.user.username, 'userId': request.user.id })

class ResourceList(APIView):
    def get(self, request, format=None):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request, format=None):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResourceDetail(APIView):
    def get_object(self, slug):
        try:
            return Resource.objects.get(slug=slug)
        except Resource.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        resource = self.get_object(slug)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data, content_type="application/json")

    def put(self, request, slug, format=None):
        resource = self.get_object(slug)
        serializer = ResourceSerializer(resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        resource = self.get_object(slug)
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ResourceFeedbackList(APIView):
    def get(self, request, slug, format=None):
        feedbacks = Feedback.objects.filter(resource__slug=slug)
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data, content_type="application/json")

class ResourceRelatoList(APIView):
    def get(self, request, slug, format=None):
        relatos = Relato.objects.filter(resource__slug=slug)
        serializer = RelatoSerializer(relatos, many=True)
        return Response(serializer.data, content_type="application/json")

class FeedbackList(APIView):
    def get(self, request, format=None):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbackDetail(APIView):
    def get_object(self, uuid):
        try:
            return Feedback.objects.get(uuid=uuid)
        except Feedback.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):
        feedback = self.get_object(uuid)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data, content_type="application/json")

    def put(self, request, uuid, format=None):
        feedback = self.get_object(uuid)
        serializer = FeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        feedback = self.get_object(uuid)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeList(APIView):
    def post(self, request, format=None):
        serializer = LikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RelatoList(APIView):
    def get(self, request, format=None):
        relatos = Relato.objects.all()
        serializer = RelatoSerializer(relatos, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request, format=None):
        serializer = RelatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RelatoDetail(APIView):
    def get_object(self, uuid):
        try:
            return Relato.objects.get(uuid=uuid)
        except Relato.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):
        relato = self.get_object(uuid)
        serializer = RelatoSerializer(relato)
        return Response(serializer.data, content_type="application/json")

    def put(self, request, uuid, format=None):
        relato = self.get_object(uuid)
        serializer = RelatoSerializer(relato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        relato = self.get_object(uuid)
        relato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
