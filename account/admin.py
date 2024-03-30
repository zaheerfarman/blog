from django.contrib import admin

# Register your models here.
from .models import BlogPost, VideoModel, ContactMessage

# Register your models here
admin.site.register(VideoModel)
admin.site.register(BlogPost)
admin.site.register(ContactMessage)