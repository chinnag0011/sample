from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=0)

class Contact(models.Model):
    mname = models.CharField(max_length=128)
    uname = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.CharField(max_length=500)


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    date_joined = models.DateField()

class Custmer(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)


