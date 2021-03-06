from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^api/resource/$', views.ResourceList.as_view()),
    url(r'^api/resource/(?P<slug>[\w-]+)/feedback/$', views.ResourceFeedbackList.as_view()),
    url(r'^api/resource/(?P<slug>[\w-]+)/relato/$', views.ResourceRelatoList.as_view()),
    url(r'^api/resource/(?P<slug>[\w-]+)/$', views.ResourceDetail.as_view()),

    url(r'^api/feedback/$', views.FeedbackList.as_view()),
    url(r'^api/feedback/(?P<uuid>[^/]+)/$', views.FeedbackDetail.as_view()),

    url(r'^api/relato/$', views.RelatoList.as_view()),
    url(r'^api/relato/(?P<uuid>[^/]+)/$', views.RelatoDetail.as_view()),

    url(r'^resource/(?P<slug>[\w-]+)/$', views.resource_detail, name='resource_detail'),

    url(r'^all/$', views.resources_list, name='resources_list'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
