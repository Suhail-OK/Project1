from django.conf.urls import url
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('signup/', v.signup, name='signup'),
    path('login/', v.userlogin, name='userlogin'),
    path('logout/', v.userlogout, name='userlogout'),
    path('hotelslist/', v.hotelslist, name='hotelslist'),
    path('foodsadd/', v.FoodAdd.as_view(), name='foodsadd'),
    path('foodslist/', v.FoodsList.as_view(), name='foodslist'),
    path('food/<pk>/', v.FoodOrderView.as_view(), name='foodorderview'),
    
]
