from django.db import models

# Create your models here.
from django.urls import reverse


class Photography(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url1 = models.CharField(max_length=100, blank=True, null=True)
    url2 = models.URLField(blank=True, null=True)
    upload_date = models.DateField(auto_now=True)
    upload_by = models.CharField(max_length=100, blank=True, null=True)
    upload_by_link = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    tag1 = models.CharField(max_length=100, blank=True, null=True)
    tag2 = models.CharField(max_length=100, blank=True, null=True)
    tag3 = models.CharField(max_length=100, blank=True, null=True)
    tag4 = models.CharField(max_length=100, blank=True, null=True)
    tag5 = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="media/contact/", blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
