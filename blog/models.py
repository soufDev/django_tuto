from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="release_date")
    category = models.ForeignKey('Category')

    def __str__(self):
        """
        this method that you define on the models,
        will allow us to recognize easily the different
        objects that we will treat on the admin panel
        """
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


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


class Offer(models.Model):
    price = models.IntegerField()
    product = models.ForeignKey(Product)
    seller = models.ForeignKey(Seller)

    def __str__(self):
        return "{0} sold by {1}".format(self.product, self.seller)


