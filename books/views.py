from os import EX_OSFILE
from books.form import ReviewForm,ReviewModelForm
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
import json
from books.models import Book,Review
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage


# Using generics
class BookListView(ListView):
    login_url='/login/'

    def get_queryset(self) :
        return Book.objects.all()


class BookDetailView(DetailView):
    model=Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.all()
        context['authors'] = context['book'].authors.all()
        #using forms.form
        # context['form']=ReviewForm()

        #using forms.modelform
        context['form']=ReviewModelForm() 
        return context


#get data from a json file
bookData = open('/Users/saurabhjj/POC/python/bookstore/books/resources/books.json').read()

data = json.loads(bookData)

#To explicitly load a url
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
    if request.user.is_authenticated:
        #option 2 with form model
        userName = request.user
        print(userName)
        singleBook = get_object_or_404(Book,pk=id)
        newReview=Review(user=userName,book_id=singleBook)
        form=ReviewModelForm(request.POST,request.FILES,instance=newReview)

        if form.is_valid():
            form.save()
        else :
            print("there is some issue")

        #option 1, without model save
        """review = request.POST['body']
        userName = request.user
        print(userName)
        singleBook = get_object_or_404(Book,pk=id)
        newReview=Review(body=review,user=userName,book_id=singleBook)

        if len(request.FILES ) != 0:
            image=request.FILES['image']
            fs = FileSystemStorage()
            name = fs.save(image.name,image)
            newReview.image=fs.url(name)

        newReview.save()"""
    return redirect(f'/book/{id}')


def author(request, author):
    books=Book.objects.filter(authors__name=author)
    context = {'book_list':books}
    return render (request,'books/book_list.html',context)