
from multiprocessing import context
from statistics import correlation
from unittest import result
from django.shortcuts import render, HttpResponse,redirect
import random 

#Post
def root(request):
    RandNum=request.session['gussednumber']
    enterednumber=request.POST['usernumber']
    #request.session['result'] = 'value'

    print("Random Number:",RandNum,enterednumber)
    if (  int(RandNum) == int(enterednumber)): #correct 
        request.session['result'] =  1
    elif ( int(RandNum) < int(enterednumber) ):  # too high
        request.session['result'] = 2
    else:   # too low
        request.session['result'] = 3
    
    return redirect('/')



#Get
def index(request):
    RandNumber=random.randint(1, 100)    #we put this here (not in the root function)to save the random before entering the enterednumber
    request.session['gussednumber'] = RandNumber
    # print(RandNum)
    # context = {
    # 'Num' : RandNum
    # }

    return render(request,'index.html')

