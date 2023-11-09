
from django.contrib import admin
from django.urls import path, include

from MyPos import views

urlpatterns = [
    path('', views.viewCategory),
    path('category/', views.viewCategory),
    path('category/store', views.storeCategory),
    path('category/findByid/<id>', views.findById)
]
