from user_model.models import User
from django.db import models

from django.contrib import admin

class Viloyat(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tuman(models.Model):
    name = models.CharField(max_length=200)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Creator')
    creators = models.ManyToManyField(User, related_name='Admins', blank=True)
    members = models.ManyToManyField(User, related_name='Members', blank=True)

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='shop_images/%Y/')
    password = models.CharField(max_length=200)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)

    lon = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @admin.display(description='Creator\'s first name')
    def ret_hos_fir(self):
        return self.host.first_name



class Types(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    image1 = models.ImageField(upload_to='products-img/')
    image2 = models.ImageField(upload_to='products-img/')
    image3 = models.ImageField(upload_to='products-img/')

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    count = models.IntegerField()
    typee = models.ForeignKey(Types, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    entry_price = models.IntegerField()
    percent = models.IntegerField()
    selling_price = models.IntegerField()
    validity_period = models.DateField(default='2006-04-02')
    enterprise = models.CharField(max_length=500)


    likes = models.IntegerField(default=0)
    seens = models.IntegerField(default=0)

    def __str__(self):
        return self.name
