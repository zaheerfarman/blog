# Create your models here.
from django.db import models
from .fields import VideoField

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject

class VideoModel(models.Model):
    title = models.CharField(max_length=100)
    video_file = VideoField(upload_to='videos/')
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1500, blank=True, null=True)
    def __str__(self):
        return str(self.id)
    
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return str(self.id)
