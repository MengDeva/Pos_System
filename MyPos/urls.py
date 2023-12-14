
from django.contrib import admin
from django.urls import path
from MyPos.controllers import Category_views,Product_views, Sale_view

urlpatterns = [
    path('', Category_views.viewCategory),
    #----- Category -----#
    path('category/', Category_views.viewCategory),
    path('category/store', Category_views.storeCategory),
    path('category/findById/<id>', Category_views.findById),
    path('category/deleteById/<id>', Category_views.deleteById),
    path('category/findByName', Category_views.findByName),
    path('category/updateById/<id>', Category_views.updateById),

    #----- Product -----#
    path('product/', Product_views.viewProduct),
    path('product/store', Product_views.storeProduct),
    # path('product/findById/<id>', Product_views.findById),
    path('product/deleteById/<id>', Product_views.deleteById),
    # path('product/findByName', Product_views.findByName),
    path('product/updateById/<id>', Product_views.updateById),

    #----- Sale -----#
    path('sale/', Sale_view.commit_data)
]