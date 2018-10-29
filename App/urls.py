from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$',views.Homepage,name='Homepage'),
    url(r'^regsiter/$',views.regsiter,name='regsiter'),
    url(r'^login/$',views.login,name='login'),
    url(r'^GoodsDetail/$',views.GoodsDetail,name='GoodsDetail'),
    url(r'^Men/$',views.Men,name='Men'),
    url(r'^shoppingbag/$',views.shoppingbag,name='shoppingbag')
]