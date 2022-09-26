
from types import CoroutineType
from unicodedata import name
from django.shortcuts import render, HttpResponse,redirect
from .models import Dojo, Ninja
def index(request):
    context={
        "all_the_dojos": Dojo.objects.all(),
        # "all_the_ninja": Ninja.objects.all(),
    }
    return render(request, 'index.html',context)

            # for dojo in context['all_the_dojos']:
                #     print(dojo.ninjas.all())


def adddojo(request):
    name1=request.POST["name"]
    city1= request.POST["city"]
    state1= request.POST["state"]
    newdojo=Dojo(name=name1, city=city1, state=state1)
    newdojo.save()
    return redirect('/')

def addninja(request):
    first_name1=request.POST["first"]
    last_name1= request.POST["last"]
    dojo1= request.POST["dojo"]

    newninja=Ninja(first_name=first_name1, last_name=last_name1,dojo=Dojo.objects.get(id=dojo1))
    newninja.save()
    return redirect('/')

# Create your views here.
