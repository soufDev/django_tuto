import os
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=42)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Release Date')

    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title


class Motor(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=25)
    motor = models.OneToOneField(Motor)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, through='Offer')

    def __str__(self):
        return self.name


def renaming(instance, name):
    file_name = os.path.splitext(name)[0]
    print(instance, name)
    return "photos/{}-{}.jpg".format(instance.id, file_name)


class Offer(models.Model):
    price = models.IntegerField()
    product = models.ForeignKey(Product)
    seller = models.ForeignKey(Seller)

    def __str__(self):
        return "{0} sold by {1}".format(self.product, self.seller)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    photo = models.ImageField(upload_to=renaming, verbose_name="Document")

    def __str__(self):
        return self.name



