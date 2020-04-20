from django.shortcuts import render,get_object_or_404

from . models import blog

def home(request):
    all_blog = blog.objects
    return render(request,'blog/index.html',{'all_blog':all_blog})

def details(request,blog_id):
    detail_blog = get_object_or_404(blog,pk= blog_id)
    return render(request,'blog/detail.html',{"detail_blog":detail_blog})