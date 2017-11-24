from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^api/resource/$', views.ResourceList.as_view()),
    url(r'^api/resource/(?P<slug>[\w-]+)/$', views.ResourceDetail.as_view()),

    url(r'^api/feedback/$', views.FeedbackList.as_view()),
    url(r'^api/feedback/(?P<uuid>[^/]+)/$', views.FeedbackDetail.as_view()),

    url(r'^resource/new/$', views.resource_new, name='resource_new'),
    url(r'^resource/all/$', views.resource_all, name='resource_all'),
    url(r'^resource/(?P<slug>[\w-]+)/$', views.resource_detail, name='resource_detail'),

    url(r'^all/$', views.resources_list, name='resources_list'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
