from django.shortcuts import render
import json
from books.models import Book


#get data from a json file
bookData = open('/Users/saurabhjj/POC/python/bookstore/books/resources/books.json').read()

data = json.loads(bookData)

# Create your views here.
def index(request):
    dbData=Book.objects.all()

    #conext from DB
    context = {'books':dbData}

    #context from json file
    #context = {'books':data}

    return render (request,'books/index.html',context)

# Create your views here.
def show(request,id):

    #data from DB
    singleBook = Book.objects.get(pk=id)


    #data from Json file
    #singleBook = list()
    #for book in data :
     #   if book['id'] == id :
      #      singleBook = book


    context = {'book':singleBook}
    return render (request,'books/show.html',context)