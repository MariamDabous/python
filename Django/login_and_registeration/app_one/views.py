from distutils.log import error
import email
from email.mime import message
from django.shortcuts import redirect, render

from django.shortcuts import render, HttpResponse,redirect

from app_one.models import users
from django.contrib import messages
import bcrypt

def register_index(request):
    return render(request, 'index.html')

def login_index(request):
    if 'userid' not in request.session:
        messages.error(request, 'You must log in first')
    else:
        context = {
            'newuser':users.objects.get(id=request.session['userid'])
        }
    return render(request, 'enter.html', context)

def register(request):
    form=request.POST
    error= users.objects.basic_validator(form)
    if len(error)>0 :
        for key,val in error.items():
            messages.error(request,val)
        return redirect('/')
    else:
        user=users.objects.create(first_name=form['fname'], last_name=form['lname'], email=form['email'],password=bcrypt.hashpw(form['pass1'].encode(),bcrypt.gensalt()).decode())
        request.session['userid']=user.id
        return redirect('/success')

def login(request):
    form= request.POST
    try:
        user= users.objects.get(email=form['email'])
    except:
        messages.error(request, 'Please check email')
        return redirect('/')
    print(form['pass'])
    print(user.password)
    if bcrypt.checkpw(form['pass'].encode(), user.password.encode())==False:
        messages.error(request, 'Please check your password')
        return redirect('/')
    request.session['userid']=user.id
    return redirect('/success')
def logout(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
