from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from loginApp.models import Avatar

# Create your views here.

def home(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request, "home/home.html", {'url':avatares[0].imagen.url})

def blog(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request, 'agenda/blog.html', {'url':avatares[0].imagen.url})

def blogpost(request):

    return render (request, 'agenda/blog-post.html')

# def agenda(request):

#     return render (request, 'agenda/index.html')

def portfolio(request):

    return render (request, 'agenda/portfolio-post.html')