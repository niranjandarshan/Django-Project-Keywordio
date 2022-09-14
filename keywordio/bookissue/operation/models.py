from django.db import models

# Create your models here.

class Book(models.Model):
    bookid=models.IntegerField()
    bookname=models.CharField(max_length=70)
    author=models.CharField(max_length=80)
    quantity=models.IntegerField()
    