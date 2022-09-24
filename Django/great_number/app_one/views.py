
from statistics import correlation
from django.shortcuts import render, HttpResponse,redirect
import random 

def root(request):
    x=random.randint(1, 100)
    request.session['gussed number'] = x
    enterednumber=request.Post['usernumber']
    request.session['result']='hi'
    if (request.session['gussed number']==enterednumber):
        request.session['result']='correct'
    else:
        if ((enterednumber<(request.session['gussed number']+10))
        or (enterednumber>(request.session['gussed number']-10) )):
            request.session['result']='Too low!'
        else:
            request.session['result']='Too High!'
    return render


    



def index(request):
    return render(request,'index.html',request.session['result'])

