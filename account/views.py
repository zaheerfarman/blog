from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, VideoModel, ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data=ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        data.save()
        

    return render(request,'account/contact.html')

def blog(request):
    post = BlogPost.objects.all()
    print(post)

    return render(request,'account/blog.html', {'post': post})

def videos(request):
    videos = VideoModel.objects.all()
    return render(request,'account/videos.html', {'videos': videos})

def about(request):
    return render(request,'account/about.html')
def home(request, posts_id):
    post = get_object_or_404(BlogPost, pk=posts_id)
    return render(request,'account/home.html', {'post': post})

def play(request, video_id):
    video = get_object_or_404(VideoModel, pk=video_id)
    return render(request,'account/play.html', {'video': video})