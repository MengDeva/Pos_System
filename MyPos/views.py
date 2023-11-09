from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from MyPos.serializers.CategorySerializers import CategorySerializer
from .models import Category
from rest_framework import status

# Create your views here.


@api_view(["GET"])
def viewCategory(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def storeCategory(request):
    category = Category()
    category.name = request.data["name"]
    category.createBy_id = request.data["createBy"]
    category.updateBy_id = request.data["updateBy"]
    category1 = Category.objects.filter(name=category.name)
    if category1:
        return Response({"message": "Category name already exists"})
    data = {
        "name": category.name,
        "createBy": category.createBy_id,
        "updateBy": category.updateBy_id
    }
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Category Created"}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def findById(request, id):
    try:
        categorys = Category.objects.get(pk=id)
        serializer = CategorySerializer(categorys, many=True)
    except Category.DoesNotExist:
        return Response({"message": "ID Not found:"+id})
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
