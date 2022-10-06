from distutils.log import error
import email
from email.mime import message
from multiprocessing import context
from django.shortcuts import redirect, render

from django.shortcuts import render, HttpResponse,redirect

from app_one.models import Tree, users
from django.contrib import messages
import bcrypt

def register_index(request):
    return render(request, 'form.html')

def login_index(request):
    if 'userid' not in request.session:
        messages.error(request, 'You must log in first')
    else:
        context = {
            'newuser':users.objects.get(id=request.session['userid']),
            'alltrees': Tree.objects.all()
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
        return redirect('/dashboard')

def login(request):
    form= request.POST
    try:
        user= users.objects.get(email=form['email'])
    except:
        messages.error(request, 'Please check email')
        return redirect('/')
    
    if bcrypt.checkpw(form['pass'].encode(), user.password.encode())==False:
        messages.error(request, 'Please check your password')
        return redirect('/')
    request.session['userid']=user.id
    return redirect('/dashboard')
def logout(request):
    request.session.clear()
    return redirect('/')

def treeform_index(request):
    context= {
        'availableuser':users.objects.get(id=request.session['userid']),
    }
    return render(request, 'treeform.html',context)

def creat_Tree(request):
    form=request.POST
    error= Tree.objects.basic_validator(form)
    if len(error)>0 :
        for key,val in error.items():
            messages.error(request,val)
        return redirect('/new/tree')
    Tree.objects.create(species=form['spieces'], location=form['location'],user=users.objects.get(id=request.session['userid']),date_planted=form['date'],reason=form['reason'])
    return redirect('/new/tree')

def mytree_index(request):
    context={
        'mytree' :Tree.objects.filter(user=users.objects.get(id=request.session['userid'])) ,
        'availableuser':users.objects.get(id=request.session['userid']),
    }
    # print('hi')
    return render(request, 'mytree.html',context)

def delete(request,treeid):
    delete_tree= Tree.objects.get(id=treeid)
    delete_tree.delete()
    return redirect('/user/account')

def edit_index(request, treeid):
    context = {
        'availableuser':users.objects.get(id=request.session['userid']),
        'edittree': Tree.objects.get(id=treeid)
    }

    return render(request, 'edit.html',context)



def edit(request,treeid):
    id=treeid
    form= request.POST
    error= Tree.objects.basic_validator(form)
    if len(error)>0 :
        for key,val in error.items():
            messages.error(request,val)
        return redirect('/edit/'+str(id))
    edit_tree=Tree.objects.get(id=treeid)
    edit_tree.species= form['spieces']
    edit_tree.location= form['location']
    edit_tree.reason= form['reason']
    edit_tree.date_planted= form['date']
    edit_tree.save()

    return redirect('/edit/'+str(id))

def show_index(request, treeid):
    context = {
        'availableuser':users.objects.get(id=request.session['userid']),
        'onetree': Tree.objects.get(id=treeid)
    }
    x= Tree.objects.get(id=treeid)
    return render(request, 'treeinfo.html',context)

# def update(request,id5):
    
#     edit_show = TVshow.objects.get(id=int(id5))
#     edit_show.title=request.POST['title']
#     edit_show.network=request.POST['net']
#     edit_show.release_date=request.POST['date']
#     edit_show.description=request.POST['desc']
#     edit_show.save()
    
#     # c = ClassName.objects.get(id=1)
#     # c.field_name = "some new value for field_name"
#     # c.save()
    
#     return redirect('/shows/'+str(id5))

# def delete1(request,id4):
#     delete_show=TVshow.objects.get(id=id4)
#     delete_show.delete()
#     return redirect('/shows')

    # c = ClassName.objects.get(id=1)
    # c.delete()

# Create your views here.
