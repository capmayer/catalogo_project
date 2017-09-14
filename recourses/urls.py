from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^recourse/(?P<slug>[\w-]+)/$', views.recourse_detail, name='recourse_detail'),
]
