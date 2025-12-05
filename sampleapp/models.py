from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    class Meta:
        db_table="Student"

class Worker(models.Model):
    name=models.CharField(max_length=50)
    job=models.IntegerField()

class Event(models.Model):
    name=models.CharField(max_length=30)
    date=models.DateField()
    description=models.CharField(max_length=50)

class Production(models.Model):
    Name=models.CharField(max_length=20)
    Price=models.IntegerField()
    Created_date=models.DateField()

class Books(models.Model):
    Title=models.CharField(max_length=50)
    Author=models.CharField(max_length=20)
    published_date=models.DateField()


class college(models.Model):
    name=models.CharField(max_length=50)
    place= models.CharField(max_length=30)
    phone=models.IntegerField()

class Image(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='media')


class Author(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField(max_length=255)


class Book_s(models.Model):
    author_id=models.ForeignKey(Author,on_delete=models.CASCADE)
    book_name=models.CharField(max_length=255)


class Trainer(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)

class Bookss(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    summary = models.TextField()
    isbn= models. CharField(max_length=13, unique=True)

class work(models.Model):
    name=models.CharField(max_length=30)
    GENDER_CHOICES=[
        ("male","male"),
        ("female","female"),
        ("others","others"),
    ]
    gender=models.CharField(choices=GENDER_CHOICES,max_length=6)