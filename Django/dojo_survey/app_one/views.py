
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def result_show(request):
    name= request.POST['name']
    location= request.POST['location']
    language=request.POST['language']
    comment=request.POST['comment']
    context = {
        "name1" : name,
        "location1" : location,
        "language": language,
        "comment1" :comment
    }
    return render(request, 'index2.html',context)
    