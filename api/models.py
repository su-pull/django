from django.db import models
from django.urls import reverse
# null=True, blank=True


class Docs(models.Model):

    title_ja = models.CharField(max_length=100)
    content_ja = models.TextField()
    description_ja = models.TextField(max_length=300)
    title_en = models.CharField(max_length=100)
    content_en = models.TextField()
    description_en = models.TextField(max_length=300)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Docs'

    def __str__(self):
        return self.title_ja


class Talk(models.Model):

    title_ja = models.CharField(max_length=100)
    content_ja = models.TextField()
    description_ja = models.TextField(max_length=300)
    title_en = models.CharField(max_length=100)
    content_en = models.TextField()
    description_en = models.TextField(max_length=300)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_ja


class Build(models.Model):

    title_ja = models.CharField(max_length=100)
    content_ja = models.TextField()
    description_ja = models.TextField(max_length=300)
    title_en = models.CharField(max_length=100)
    content_en = models.TextField()
    description_en = models.TextField(max_length=300)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_ja

