from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^resource/new/$', views.resource_new, name='resource_new'),
    url(r'^resource/(?P<slug>[\w-]+)/$', views.resource_detail, name='resource_detail'),
    url(r'^all/$', views.resources_list, name='resources_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)