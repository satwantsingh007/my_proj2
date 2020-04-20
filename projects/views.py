from django.shortcuts import render,get_object_or_404
from . models import project
# Create your views here.

def home(request):
    projects = project.objects
    return render(request,'proj/index.html',{'project':projects})

def detail(request,proj_id):
    detail_proj = get_object_or_404(project,pk = proj_id)
    return render(request,'proj/details.html',{'detail_proj':detail_proj})