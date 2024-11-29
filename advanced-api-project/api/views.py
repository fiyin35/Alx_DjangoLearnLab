from django.shortcuts import render
from .models import Book

# Create your views here.
def ListView(request):
    '''retrieve all the books stored in the database'''
    books = Book.objects.all()
    return books

def DetailView(request):
    pass

def CreateView(request):
    pass

def UpdateView(request):
    pass 

def DeleteView(request):
    pass