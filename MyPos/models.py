import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True, null=False)
    createBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Category")
    updateBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True, null=True, blank=True)
    barcode = models.BigIntegerField(null=True, unique=True)
    unitPrice = models.FloatField()
    qtyInstock = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="media/")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="Product")
    createBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Product")
    updateBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    PurchaseDate = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="Purchase")
    qty = models.IntegerField()
    cost = models.FloatField()
    total = models.FloatField()
    createBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Purchase")


class Sale(models.Model):
    saleDate = models.DateTimeField(auto_now_add=True)
    createBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Sale")
    totalAmount = models.FloatField()


class SaleDetail(models.Model):
    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE, related_name="SaleDetail")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="SaleDetail")
    qty = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
