from django.db import models

# Create your models here.


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
    tags = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
