from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
import json
from books.models import Book,Review


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
    try:
        singleBook = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')

    #inbuilt exception handlig
    singleBook = get_object_or_404(Book,pk=id)
    reviews=Review.objects.filter(book_id=id).order_by('-created_at')

    #data from Json file
    #singleBook = list()
    #for book in data :
     #   if book['id'] == id :
      #      singleBook = book


    context = {'book':singleBook,'reviews':reviews}
    return render (request,'books/show.html',context)


def review(request,id):
    review = request.POST['review']
    newReview=Review(body=review,book_id=id)
    newReview.save()
    return redirect('/book')