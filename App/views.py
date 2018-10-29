from django.shortcuts import render

# Create your views here.
# 首页
def Homepage(request):
    return render(request,'Homepage.html')

# 注册
def regsiter(request):
    return render(request,'regsiter.html')

# 登陆
def login(request):
    return render(request,'login.html')

# 购物车
def shoppingbag(request):
    return render(request,'shoppingbag.html')

#
def GoodsDetail(request):
    return render(request,'GoodsDetails.html')


def Men(request):
    return render(request,'Men.html')