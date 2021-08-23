from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#Dummy data
posts = [
    {
        'authour': 'nkem',
        'title' : 'Blog post',
        'content' : 'First post content',
        'date_posted' : 'August 17, 2021' 
    },
    {
        'authour': 'john',
        'title' : 'Blog post2',
        'content' : 'ttFirst post content',
        'date_posted' : 'August 67, 2021' 
    }
]

# The home function to handle traffic from the home page of the blog

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
 
 # The about function to handle traffic from the about page of the blog

def about (request):
    return render(request, 'blog/about.html', {'title': 'About'})
    