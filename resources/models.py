from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

import uuid

from hitcount.models import HitCount, HitCountMixin
from autoslug import AutoSlugField

def image_location(instance, filename):
    return '%s/image/%s' % (instance.resource.slug, filename)

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class Deslike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class Resource(models.Model, HitCountMixin):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)

    DIFFICULTS = (
        ('in', 'Iniciantes'),
        ('me', 'Intermediários'),
        ('av', 'Avançados'),
        ('id', 'Indefinido')
    )
    difficult_education = models.CharField(max_length=2, choices=DIFFICULTS, default='id')
    difficult_student = models.CharField(max_length=2, choices=DIFFICULTS, default='id')

    value = models.FloatField(blank=True, null=True)
    url = models.CharField(max_length=150, blank=True, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True)
    languages = models.ManyToManyField(Language, blank=True)

    resources = models.ManyToManyField("self", blank=True)

    slug = AutoSlugField(populate_from='title', null=True)

    likes = models.ManyToManyField(Like, blank=True)
    deslikes = models.ManyToManyField(Deslike, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    hit_count_generic = GenericRelation(
        HitCount, object_id_field='id',
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

class Image(models.Model):
    resource = models.ForeignKey(Resource)
    is_main = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_location)

class Feedback(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=600)
    is_pro = models.BooleanField(default=True)

    likes = models.ManyToManyField(Like, blank=True)
    deslikes = models.ManyToManyField(Deslike, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    last_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.description

class Relato(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)

    likes = models.ManyToManyField(Like, blank=True)
    deslikes = models.ManyToManyField(Deslike, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    last_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.author.username
