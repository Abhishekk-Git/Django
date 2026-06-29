from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Create your views here.
def blogs(request):
    context = {
        'title': 'My Blog',
        'content': 'Welcome to my blog!',
        'skills': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
    }
    return render(request, 'blog/blog.html', context)