from django.urls import path

from hrs import views

urlpatterns = [
  path('', views.index, name='index')
] 
# path函数是Django 2.x中新添加的函数，除此之外还可以使用支持正则表达式的URL映射函数re_path函数；Django 1.x中是用名为url函数来设定URL映射。