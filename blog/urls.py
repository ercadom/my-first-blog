from django.urls import path
from . import views

# 例）ブラウザにhttp://127.0.0.1:8000/post/5/を入力すると、
# Djangoはpost_detailというビューを探していると理解します。
# そしてpkが5という情報をそのビューに転送します。

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]