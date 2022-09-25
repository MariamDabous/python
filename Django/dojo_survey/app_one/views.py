
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def result_show(request):
    location1= request.POST['location']
    language1=request.POST['language']
    comment1=request.POST['comment']
    request.session['name12']=request.POST['name']  #we can write anyname inside the key but we have to use it in all of this project
    request.session['location12']=location1         #we can write the post and session in one line but it is not prefferable in coding(like the previous line)
    request.session['language12']=language1
    request.session['comment12']=comment1
    return redirect('/result2')

def result2_show(request):
    return render(request, 'index2.html')


    