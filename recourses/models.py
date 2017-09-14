from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models
from autoslug import AutoSlugField

def image_location(instance, filename):
    return '%s/image/%s' % (instance.recourse.slug, filename)

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class Recourse(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=255)

    DIFFICULTS = (
        ('in', 'Iniciantes'),
        ('me', 'Intermediários'),
        ('av', 'Avançados'),
        ('id', 'Indefinido')
    )
    difficult_education = models.CharField(max_length=2, choices=DIFFICULTS, default='op')
    difficult_student = models.CharField(max_length=2, choices=DIFFICULTS, default='op')

    value = models.FloatField(blank = True, null = True)
    url = models.CharField(max_length=150, blank = True, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, blank = True)
    languages = models.ManyToManyField(Language, blank = True)

    recourses = models.ManyToManyField("self", blank = True)

    slug = AutoSlugField(populate_from='title', null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class Photos(models.Model):
    recourse = models.ForeignKey(Recourse)
    is_main = models.BooleanField(default = False)
    image = models.ImageField(upload_to=image_location, null=True, blank=True)

class Feedback(models.Model):
    recourse = models.ForeignKey(Recourse, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title + " by: " + self.author.username

class Pro(models.Model):
    title = models.CharField(max_length=150)
    recourse = models.ForeignKey(Recourse)

    def __str__(self):
        return self.title

class Con(models.Model):
    title = models.CharField(max_length=150)
    recourse = models.ForeignKey(Recourse)

    def __str__(self):
        return self.title
