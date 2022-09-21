from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if "counter" not in request.session:
        request.session['counter']=0
    request.session['counter']+=1
    return render(request, "index.html")

def destroy(request):
    del request.session['counter']
    return redirect('/')

def add(request):
    request.session['counter']+=1
    return redirect('/')
def addnum(request,number):
    request.session['counter']+=number-1
    return redirect('/')

