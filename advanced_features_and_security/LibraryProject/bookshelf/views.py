from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def createBook(request):
    if request.method == 'POST':
        pass
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def editBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        pass

@permission_required('bookshelf.can_view', raise_exception=True)
def viewBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        pass

@permission_required('bookshelf.can_create', raise_exception=True)
def deleteBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        pass

