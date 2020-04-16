from django.shortcuts import render
from projects.models import project

def home(request):
    projects = project.objects
    return render(request,'index.html',{"project":projects})