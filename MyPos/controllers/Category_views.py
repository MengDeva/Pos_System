import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from MyPos.serializers.CategorySerializers import CategorySerializer
from MyPos.models import Category
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
        serializer = CategorySerializer(categorys)
    except Category.DoesNotExist:
        return Response({"message": "ID Not found:"+id})
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def findByName(request):
        category1=Category()
        category1.name=request.data['name']
        category = Category.objects.filter(name=category1.name)
        if category.count()==0:
            return Response({"message":"Category name Not found: "+category1.name})
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(["GET","DELETE"])
def deleteById(request,id):
    category = Category.objects.filter(id=id)
    if category.count()==0:
        return Response({"message":"Id Not Found: "+id})
    category.delete()
    return Response({"message": "Category deleted"},status=status.HTTP_200_OK)

@api_view(["GET","PUT"])
def updateById(request,id):
    try:
        category=Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response({"message": "ID Not found: " + id})
    category.name=request.data["name"]
    category.updateBy_id=request.data["updateBy"]
    category.updateAt=datetime.datetime.now()
    data={
            "name": category.name,
            "updateBy": category.updateBy_id,
            "updateAt": category.updateAt
    }
    serializer=CategorySerializer(category,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Category Updated"}, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)
