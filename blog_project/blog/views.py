from django.http import HttpResponse
from django.shortcuts import render
from . models import Post


def home_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/base.html", context)

def about(request):
    return render(request, "blog/about.html")

