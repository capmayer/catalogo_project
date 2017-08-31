from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models

def image_location(instance, filename):
    return '%s/image/%s' % (instance.slug, filename)

class Tool(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title + " by: " + self.author.username

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    DIFFICULTS = (
        ('in', 'Iniciantes'),
        ('me', 'Intermediários'),
        ('av', 'Avançados'),
        ('id', 'Indefinido')
    )
    difficult = models.CharField(max_length=2, choices=DIFFICULTS, default='op')
    value = models.FloatField(blank = True)
    url = models.CharField(max_length=150, blank = True)
    image = models.ImageField(upload_to=image_location, null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    tools = models.ManyToManyField(Tool)
    tags = models.ManyToManyField(Tag)

    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class Pro(models.Model):
    title = models.CharField(max_length=150)
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.title

class Con(models.Model):
    title = models.CharField(max_length=150)
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.title
