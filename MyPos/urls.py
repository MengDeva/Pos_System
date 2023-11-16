
from django.contrib import admin
from django.urls import path, include

from MyPos import views

urlpatterns = [
    path('', views.viewCategory),
    path('category/', views.viewCategory),
    path('category/store', views.storeCategory),
    path('category/findById/<id>', views.findById),
    path('category/deleteById/<id>', views.deleteById),
    path('category/findByName', views.findByName),
    path('category/updateById/<id>', views.updateById),
]
