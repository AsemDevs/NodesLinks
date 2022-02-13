from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('v1/', views.v1, name="v1"), 
    path('', views.home, name="home"), 
    path('first/upload/', views.upload_csv,name='upload_csv'),
    # path('start/', views.index, name="index"), 
]
