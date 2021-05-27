from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name=models.CharField(max_length=256)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(null=True)
    thumbnailUrl = models.CharField(max_length=256,null=True)
    shortDescription = models.CharField(max_length=500,null=True)
    longDescription = models.TextField(null=True)
    isbn=models.CharField(max_length=256,null=True)
    publishedDate=models.CharField(max_length=256,null=True)
    status=models.CharField(max_length=256,null=True)
    authors=models.TextField(null=True)
    categories=models.TextField(null=True)
    authors=models.ManyToManyField(Author)

    def __str__(self):
        return self.title




class Review(models.Model):
    body=models.TextField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now=True)
    book_id=models.ForeignKey(Book,on_delete=models.CASCADE)



