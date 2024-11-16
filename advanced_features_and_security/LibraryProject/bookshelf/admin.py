from django.contrib import admin
from django.db import models
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')

    search_fields = ('author', 'title')



admin.site.register(Book, BookAdmin)