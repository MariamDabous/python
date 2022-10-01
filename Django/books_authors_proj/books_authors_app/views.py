
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    context = {
        "all_books" : Book.objects.all(),
        
    }
    
    return render(request, 'book.html',context)

def Addbook(request):
    title1=request.POST['title']
    description1= request.POST['description']
    Book.objects.create(title=title1, desc=description1 )

    return redirect('/')

def index1(request):
    context = {
        "all_authors" : Author.objects.all(),
    }
    
    return render(request, 'author.html',context)

def Addauthor(request):
    f_name=request.POST['first']
    l_name= request.POST['last']
    note= request.POST['notes']
    Author.objects.create(first_name=f_name, last_name=l_name, notes=note )

    return redirect('/authors')


def bookdesc(request, id):
    request.session['id']=id
    Book.objects.get(id=id)
    context= {
        "all_book" : Book.objects.get(id=id),
        "the_author" :Book.objects.get(id=id).publishers.all(),
        "all_authors" : Author.objects.exclude(books=id)
    }
    return render(request, 'bookdescription.html',context)

def selectonauthor(request):
    id_for_author=request.POST['select1'] 
    id2=request.session['id']
    this_book= Book.objects.get(id=id2)
    this_auther=Author.objects.get(id=id_for_author)
    this_book.publishers.add(this_auther)
    return redirect('/books/'+str(id2))
# Create your views here.
def authordesc(request,id):
    request.session['id_for_author']=id
    Author.objects.get(id=id)
    context = {
        "author_desc":Author.objects.get(id=id),
        "Books_for_author":Author.objects.get(id=id).books.all(),
        "all_book" : Book.objects.exclude(publishers=id)
    }
    return render(request, 'authordescription.html', context)

def selectbook(request):
    id_for_author=request.session['id_for_author']
    id_for_book= request.POST['select1']
    Book.objects.get(id=id_for_book).publishers.add(Author.objects.get(id=id_for_author))
    return redirect('/author/'+str(id_for_author))