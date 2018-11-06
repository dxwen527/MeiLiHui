from django.shortcuts import render

# Create your views here.
# 首页
from App.models import Good, GoodsDetail


def Homepage(request):
    return render(request,'Homepage.html')

# 注册
def regsiter(request):
    # if request.method == 'GET': # 获取注册页面
        return render(request,'regsiter.html')
    # elif request.method == 'POST': # 注册操作
    #     # 获取客户端传入的数据
    #     username = request.POST.get('username')
    #     passWordtext = request.POST.get('passWordtext')
    #     print(username)

# 登陆
def login(request):
    return render(request,'login.html')

# 购物车
def shoppingbag(request):
    return render(request,'shoppingbag.html')

#
def GoodsDetails(request,goodsid):
    goodsdetail = GoodsDetail.objects.filter(goodid=goodsid)
    date = {
        'goodsdetail':goodsdetail
    }
    return render(request,'GoodsDetails.html',context=date)


def Men(request):
    goods = Good.objects.all()
    date = {
        'goods': goods,
    }
    return render(request,'Men.html',context=date)