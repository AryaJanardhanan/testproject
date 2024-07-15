from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default=0)
    last_name = models.CharField(max_length=100, default=0)
    username = models.CharField(max_length=100, default=0)
    email = models.EmailField(max_length=100, default=0)

    def __str__(self):
        return self.user.username
    

class Item(models.Model):
    name = models.CharField(max_length=100)
    des = models.TextField(max_length=400)
    image = models.ImageField(upload_to='images/', default=0)
    document = models.FileField(upload_to='documents/', default=0)

    def __str__(self):
        return self.name


class Userr(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()


class Userprofile(models.Model):
    user = models.OneToOneField(Userr, on_delete=models.CASCADE)




class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


#Querying data
# CRUD Operations

#data = Book.objects.all()
#       Book.objects.filter(author="ghwdcjxs")

#obj = Book(field1='fgh', field2='hfcvgb')
#obj.save()

#obj.field1 = 'gfh'
#obj.save()
#obj.delete()
