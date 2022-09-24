

from django.shortcuts import render, HttpResponse,redirect

from .models import users

def index(request):
    context = {
        "all_the_users": users.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    # users.objects.create(first_name=request.POST.get.first,last_name=request.POST.get.last,email_address=request.POST.get.email,age=request.POST.get.age)
    first= request.POST["first"]
    last = request.POST["last"]
    email = request.POST["email"]
    age = request.POST["age"]
    newuser=users(first_name=first, last_name=last, email_address=email, age=age)
    newuser.save()
    return redirect("/")


