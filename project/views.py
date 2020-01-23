from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import operator
from .models import Project

def home(request):
    Projects = Project.objects
    return render(request , 'project/home.html' ,  {'Projects':Projects})

def detail(request , project_id):
    project = get_object_or_404(Project,pk=project_id)
    return render(request,'project/detail.html',{'project':project})