
from django.shortcuts import render
from .models import Blog


def get_info(request):
    blogs=Blog.objects.all()
    context={
        'u':blogs
    }
    return render(request,'blog/info.html',context)


