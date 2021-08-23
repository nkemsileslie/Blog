from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# The home function to handle traffic from the home page of the blog

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
 
 # The about function to handle traffic from the about page of the blog

def about (request):
    return render(request, 'blog/about.html', {'title': 'About'})
    