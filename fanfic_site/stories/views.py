from django.shortcuts import render
from django.http import HttpResponse
from .models import Story



def home(request):
    context = {
        'stories': Story.objects.all()
    }
    return render(request, 'stories/home.html', context)

def about(request):
    return render(request, 'stories/about.html', {'title': 'About'})