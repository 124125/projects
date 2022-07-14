from django.shortcuts import render
from .models import Subjects,Mathsb,Physicsb,Englishb,Beb,Bmeb,Bmewb,Bewb,Ecwb
# Create your views here.
    
#hello


def home(request):
    subjectslist = Subjects.objects.all()
    context = {"subjectslist":subjectslist}
    return render(request,'books/index.html',context)


#books pages
def maths(request):
    subjectslist = Mathsb.objects.all()
    context = {"bookslist":subjectslist}
    return render(request,'books/books.html',context)
    
def physics(request):
    subjectslist = Physicsb.objects.all()
    context = {"bookslist":subjectslist}
    return render(request,"books/books.html",context)

def english(request):
    subjectslist = Engliahb.objects.all()
    context = {"bookslist":subjectslist}
    return render(request,"books/books.html",context)

def be(request):
    subjectslist = Beb.objects.all()
    context = {"bookslist":subjectslist}
    return render(request,"books/books.html",context)

def bme(request):
    subjectslist = Bmeb.objects.all()
    context = {"bookslist":subjectslist}
    return render(request,"books/books.html",context)

def bmew(request):
    subjectslist = Bmewb.objects.all()
    context = {"bookslist":subjectslist}
    return render(request,"books/books.html",context)

def bew(request):
    subjectslist = Bewb.objects.all()
    context = {"bookslist":subjectslist}
    return render(request,"books/books.html",context)

def ecw(request):
    subjectslist = Ecwb.objects.all()
    context = {"bookslist":subjectslist}
    return render(request,"books/books.html",context)
