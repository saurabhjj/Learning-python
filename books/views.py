from django.shortcuts import render
import json

bookData = open('/Users/saurabhjj/POC/python/bookstore/books/resources/books.json').read()

data = json.loads(bookData)

# Create your views here.
def index(request):
    context = {'books':data}
    return render (request,'books/index.html',context)

# Create your views here.
def show(request,id):
    context = {'books':data}
    return render (request,'books/show.html',context)