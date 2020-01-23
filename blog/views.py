from django.shortcuts import render
from django.http import HttpResponse
import operator


def home(request):
    return render(request , 'blog/home.html' )