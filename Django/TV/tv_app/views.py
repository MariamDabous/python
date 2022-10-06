from turtle import title
from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect
from .models import TVshow
from django.contrib import messages
from models import *

def index(request):
    context ={
        'all_shows':TVshow.objects.all()
    }
    return render(request,'readall.html', context)

def index2(request):
    context ={
        'all_shows' : TVshow.objects.all()
    }
    return render(request, 'create.html')

def index3(request,id5):
    context ={
        'one_show' : TVshow.objects.get(id=int(id5))
    }
    return render(request, 'read(one).html', context)

def create(request):
    information= request.POST
    errors=TVshow.objects.basic_validator(information)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request,val)
        return redirect('/shows/new')

    models.createTVShow(request)
    last1=  TVshow.objects.last() 
    id1=last1.id
    return redirect('/shows/'+str(id1))


#namming functions and var should be descrptive 

def index4(request,id5):
    context ={
        'edit_show' : TVshow.objects.get(id=int(id5))
    }
    return render(request, 'edit.html', context)

#This function will do ....
def update(request,id5):
    
    edit_show = TVshow.objects.get(id=int(id5))
    edit_show.title=request.POST['title']
    edit_show.network=request.POST['net']
    edit_show.release_date=request.POST['date']
    edit_show.description=request.POST['desc']
    edit_show.save()
    
    # c = ClassName.objects.get(id=1)
    # c.field_name = "some new value for field_name"
    # c.save()
    
    return redirect('/shows/'+str(id5))

def delete1(request,id4):
    delete_show=TVshow.objects.get(id=id4)
    delete_show.delete()
    return redirect('/shows')

    # c = ClassName.objects.get(id=1)
    # c.delete()
# Create your views here.
