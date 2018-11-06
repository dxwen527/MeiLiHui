from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    passWordtext = models.CharField(max_length=256)


class Good(models.Model):
    mai = models.CharField(max_length=20)
    img = models.CharField(max_length=50)
    alt = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    p1 = models.CharField(max_length=50)
    p2 = models.CharField(max_length=50)
    span1 = models.CharField(max_length=20)
    span2 = models.CharField(max_length=20)
    goodsid = models.CharField(max_length=20)

class GoodsDetail(models.Model):
    goodid = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    product = models.CharField(max_length=256)
    bigImg = models.CharField(max_length=100)
    alt = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    smallimg1 = models.CharField(max_length=100)
    smallimg2 = models.CharField(max_length=100)
    smallimg3 = models.CharField(max_length=100)
    producttitle = models.CharField(max_length=100)
    productname = models.CharField(max_length=256)
    currentprice = models.CharField(max_length=100)
    originalprice = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    selectimg = models.CharField(max_length=100)
    selectcolor = models.CharField(max_length=100)
    choosesize1 = models.CharField(max_length=100)
    choosesize2 = models.CharField(max_length=100)
    choosesize3 = models.CharField(max_length=100)
    changtu = models.CharField(max_length=100)