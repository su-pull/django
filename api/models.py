from django.db import models
from django.urls import reverse


class Docs(models.Model):

    title_ja = models.CharField(max_length=100)
    content_ja = models.TextField()
    description_ja = models.TextField(null=True, blank=True)
    title_en = models.CharField(max_length=100)
    content_en = models.TextField(null=True, blank=True)
    description_en = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Docs'

    def __str__(self):
        return self.title_ja


class Talk(models.Model):

    title_ja = models.CharField(max_length=100)
    content_ja = models.TextField()
    description_ja = models.TextField(null=True, blank=True, default="")
    title_en = models.CharField(max_length=100)
    content_en = models.TextField()
    description_en = models.TextField(null=True, blank=True, default="")
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_ja

