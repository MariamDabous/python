from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect
import random
from time import localtime, strftime
def index(request):
    return render(request, 'index.html')

def results(request):
    if "gold" not in request.session:
        request.session['gold']=0
        request.session['logs']=[]

    if request.POST['which_one'] == 'farm':
        farmgold=random.randint(10,20)
        request.session['gold']+=farmgold
        current_log={
            "message":(f"You entered a farm and earned {farmgold} gold. ({strftime('%b %d, %Y %I:%M %p', localtime())})")
        }
        request.session['logs'].append(current_log)
        request.session.save()


    elif request.POST['which_one'] == 'cave':
        cavegold=random.randint(10,20)
        request.session['gold']+=cavegold
        current_log={
            "message":(f"You entered a cave and earned {cavegold} gold. ({strftime('%b %d, %Y %I:%M %p', localtime())})")
        }
        request.session['logs'].append(current_log)
        request.session.save()

    elif request.POST['which_one'] == 'house':
        housegold=random.randint(10,20)
        request.session['gold']+=housegold
        current_log={
            "message" : (f"You entered a house and earned {housegold} gold. ({strftime('%b %d, %Y %I:%M %p', localtime())})")
        }
        request.session['logs'].append(current_log)
        request.session.save()

    elif request.POST['which_one'] == 'quest':
        questgold=random.randint(-50,50)
        request.session['gold']+=questgold
        status: "earned" if questgold>=0 else "lost"
        current_log={
            "status": "earned" if questgold>=0 else "lost",
            "message":(f"You entered a quest and {status} {abs(questgold)} gold. ({strftime('%b %d, %Y %I:%M %p', localtime())})")
        }
        request.session['logs'].append(current_log)
        request.session.save()

    return redirect('/')

    #we can write the first three in one line like this:
    #if 'farm' or 'cave'  or 'house'in request.POST:
    #earn=random.randint(10,20)

# Create your views here.
