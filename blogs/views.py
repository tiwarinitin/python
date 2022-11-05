
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    # Post.objects.create(title=request.get.POST('title'),)
    all_posts = Post.objects.all()
    for x in all_posts:
        print(x.title)
        print(x.author)
        print(x.content)
        print(x.status)
        print(x.publish)

    print(all_posts)
    return render(request, 'index.html')