from distutils.log import error
import email
from email.mime import message
from turtle import tilt, title
from typing import Counter
from django.shortcuts import redirect, render

from django.shortcuts import render, HttpResponse,redirect

from app_one.models import Book, users
from django.contrib import messages
import bcrypt

def register_index(request):
    return render(request, 'index.html')

def login_index(request):
    if 'userid' not in request.session:
        messages.error(request, 'You must log in first')
    else:
        newuser=users.objects.get(id=request.session['userid'])
        context = {
            'newuser':users.objects.get(id=request.session['userid']),
            'allbook' : Book.objects.all(),
            'favbook':newuser.liked_books.all()
            
        }
        favbook=newuser.liked_books.all()
        print(favbook)
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
        return redirect('/books')

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
    return redirect('/books')
def logout(request):
    request.session.clear()
    return redirect('/')

def AddBook(request):
    form=request.POST
    error= Book.objects.basic_validator(form)
    if len(error)>0 :
        for key,val in error.items():
            messages.error(request,val)
        return redirect('/books')
    else:
        useruploadthebook=users.objects.get(id=request.session['userid'])
        Addedbook=Book.objects.create(title=form['title'],description=form['desc'], uploaded_by=useruploadthebook)
        Addedbook.users_who_like.add(useruploadthebook)
        return redirect('/books')
    
def oneBook_index(request,id):
    
    request.session['onebook_id']=id
    user_id=request.session['userid']
    context={
        'availableuser':users.objects.get(id=user_id),
        'onebook': Book.objects.get(id=id),
        'users_who_liked_one_book' : Book.objects.get(id=id).users_who_like.all(),
        'counter' : [1,2]
    }   
    
    print('hi')
    # x=Book.objects.get(id=id).users_who_like.all()
    # print(x)
    print(context['counter'])
    
    return render(request, 'onebook.html', context)

def newdesc(request):
    id=request.session['onebook_id']
    book_to_update=Book.objects.get(id=id)
    desc=request.POST['desc1']
    book_to_update.description=desc
    title=request.POST['title1']
    book_to_update.title= title
    book_to_update.save()
    return redirect('/books/'+str(id))

def unfav(request):
    book_id=request.session['onebook_id']
    user_id=request.session['userid']
    user_to_unfav= users.objects.get(id=user_id)
    book_unfav= Book.objects.get(id=book_id)
    book_unfav.users_who_like.remove(user_to_unfav)
    return redirect('/books/'+str(book_id))

def addfav(request,id2):
    # book_id=request.session['onebook_id']
    user_id=request.session['userid']
    user_to_fav= users.objects.get(id=user_id)
    book_fav= Book.objects.get(id=id2)
    book_fav.users_who_like.add(user_to_fav)
    print('hellllllo')

    return redirect('/books')

def addfav2_on_onebook_page(request,id2):
    user_id=request.session['userid']
    user_to_fav= users.objects.get(id=user_id)
    book_fav= Book.objects.get(id=id2)
    book_fav.users_who_like.add(user_to_fav)
    return redirect('/books/'+str(id2))



def delete(request):
    id4=request.session['onebook_id']
    delete_show=Book.objects.get(id=id4)
    delete_show.delete()
    return redirect('/books')



# Create your views here.
