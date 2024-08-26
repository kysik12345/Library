from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    mod = Author.objects.all()
    context = {
        'mod': mod
    }
    return render(request, 'library/index.html', context=context)

def show(request):
    myd = Book.objects.all()
    context = {
        'myd': myd
    }
    return render(request, 'library/show.html', context=context)


def add(request):

    form = AuthorForms()

    if request.method == "POST":
        form = AuthorForms(data=request.POST)
        if form.is_valid():
            author = Author()
            author.name = form.cleaned_data['name']
            author.lastname = form.cleaned_data['lastname']
            author.patronymic = form.cleaned_data['patronymic']
            author.date = form.cleaned_data['date']
           
            author.save()

            return index(request)

    context = {
        'form': form,
        'title':'Добавление автора'
    }
    return render(request, 'library/add.html', context)

def addbook(request):

    form = BookForms()

    if request.method == "POST":
        form = BookForms(data=request.POST)
        if form.is_valid():
            book = Book()
            book.author = form.cleaned_data['author']
            book.name = form.cleaned_data['name']
            book.genre = form.cleaned_data['genre']
            book.date = form.cleaned_data['date']
           
            book.save()

            return show(request)

    context = {
        'form': form,
        'title':'Добавление книги'
    }
    return render(request, 'library/addbook.html', context)