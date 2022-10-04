from distutils.log import error
import email
from email.mime import message
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render

from django.shortcuts import render, HttpResponse,redirect

from app_one.models import comment, message12, users
from django.contrib import messages
import bcrypt

def register_index(request):
    return render(request, 'index.html')

def login_index(request):
    if 'userid' not in request.session:
        messages.error(request, 'You must log in first')

    context = {
        'newuser':users.objects.get(id=request.session['userid']),
        'postmessage': message12.objects.all().order_by("-created_at"),
        'postcomment' : comment.objects.all()
        }
    return render(request, 'wall.html', context)

def postmessage(request):
    form=request.POST
    posteduser=users.objects.get(id=request.session['userid'])
    message12.objects.create(message=form['message11'],user1=posteduser)
    
    return redirect('/wall')

def postcomment(request):
    form=request.POST
    commenteduser=users.objects.get(id=request.session['userid'])
    messagecommentedon= message12.objects.get(id=request.POST['which_form'])
    print(messagecommentedon)
    x=comment.objects.create(comment7=form['comment11'],user2=commenteduser,message2=messagecommentedon)
    return redirect('/wall')

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
        return redirect('/wall')

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
    return redirect('/wall')
def logout(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
