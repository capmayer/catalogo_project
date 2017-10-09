from django.contrib import admin
from .models import Tag, Feedback, Resource, Language, Image

admin.site.register(Resource)
admin.site.register(Tag)
admin.site.register(Language)
admin.site.register(Feedback)
admin.site.register(Image)
