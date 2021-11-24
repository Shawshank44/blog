from django.shortcuts import redirect, render
from .models import *
from .form import Comments
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.htm',{'posts':posts})


def post(request,slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = Comments(request.POST)
        
        if form.is_valid():
            coment = form.save(commit=False)
            coment.post = post
            coment.save()

            return redirect('post',slug=post.slug)
    else:
        form = Comments()
    return render(request,'blog/post.htm',{'post':post , 'form': form})
