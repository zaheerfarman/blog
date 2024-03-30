from django.urls import path
from . import views
urlpatterns = [
    path('blog',views.blog, name="blog"),
    path('videos',views.videos, name="videos"),
    path('contact',views.contact, name="contact"),
    path('about',views.about, name="about"),
    path('home/<int:posts_id>/', views.home, name='home'),
    path('video/<int:video_id>/', views.play, name='play'),
]
