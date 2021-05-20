from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(null=True)
    thumbnailUrl = models.CharField(max_length=256,null=True)
    shortDescription = models.CharField(max_length=256,null=True)
    longDescription = models.TextField(null=True)
    isbn=models.CharField(max_length=256,null=True)
    publishedDate=models.CharField(max_length=256,null=True)
    status=models.CharField(max_length=256,null=True)
    authors=models.TextField(null=True)
    categories=models.TextField(null=True)