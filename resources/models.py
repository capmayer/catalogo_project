from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models
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

class Resource(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=255)

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

    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class Photo(models.Model):
    resource = models.ForeignKey(Resource, default=None)
    is_main = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_location, null=True, blank=True)

class Feedback(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    anonymous = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    is_pro = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title + " by: " + self.author.username
