from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^recourse/new/$', views.recourse_new, name='recourse_new'),
    url(r'^recourse/(?P<slug>[\w-]+)/$', views.recourse_detail, name='recourse_detail'),
    url(r'^all/$', views.recourses_list, name='recourses_list'),

]
