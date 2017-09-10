from django.contrib import admin
from .models import Tag, Feedback, Recourse, Pro, Con, Language, Photos

admin.site.register(Recourse)
admin.site.register(Tag)
admin.site.register(Language)
admin.site.register(Feedback)
admin.site.register(Pro)
admin.site.register(Con)
admin.site.register(Photos)
