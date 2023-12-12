
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from MyPos.serializers.ProductSerializers import ProductSerializer
from MyPos.models import Product,Category
from rest_framework import status

# Create your views here.
@api_view(["GET"])
def viewProduct(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
def storeProduct(request):
    try:
        product = Product()
        product.name = request.data["name"]
        product1 = Product.objects.filter(name=product.name)
        if product1:
            return Response({"message": "Product name already exists"})
        product.barcode = request.data["barcode"]
        product.sellPrice = request.data["sellPrice"]
        product.qtyInstock = request.data["qtyInstock"]
        product.category_id = request.data["category"]
        product.createBy_id = request.data["createBy"]
        if len(request.data["photo"]) > 0:
            product.photo = request.data["photo"]
            product.save()
            return Response({"message": "Product Created"}, status=status.HTTP_201_CREATED)
        else:
            product.photo = ""
            product.save()
            return Response({"message": "Product Created"}, status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response({"Error": +str(ex)},status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET"])
# def findById(request, id):
#     try:
#         categorys = Category.objects.get(pk=id)
#         serializer = CategorySerializer(categorys)
#     except Category.DoesNotExist:
#         return Response({"message": "ID Not found:"+id})
#     return JsonResponse(serializer.data, status=status.HTTP_200_OK)
#
# @api_view(["POST"])
# def findByName(request):
#         category1=Category()
#         category1.name=request.data['name']
#         category = Category.objects.filter(name=category1.name)
#         if category.count()==0:
#             return Response({"message":"Category name Not found: "+category1.name})
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
@api_view(["GET","DELETE"])
def deleteById(request,id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({"message": "ID Not Found:" + id})
    if product.photo:
        product.photo.delete()
        product.delete()
        return Response({"message": "Product Deleted"},status=status.HTTP_201_CREATED)
    else:
        product.delete()
        return Response({"message": "Product Deleted"}, status=status.HTTP_201_CREATED)

# @api_view(["GET","PUT"])
# def updateById(request,id):
#     try:
#         category=Category.objects.get(pk=id)
#     except Category.DoesNotExist:
#         return Response({"message": "ID Not found: " + id})
#     category.name=request.data["name"]
#     category.updateBy_id=request.data["updateBy"]
#     category.updateAt=datetime.datetime.now()
#     data={
#             "name": category.name,
#             "updateBy": category.updateBy_id,
#             "updateAt": category.updateAt
#     }
#     serializer=CategorySerializer(category,data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Category Updated"}, status=status.HTTP_200_OK)
#     return Response(serializer.data, status=status.HTTP_200_OK)
