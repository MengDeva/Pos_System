from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from MyPos.models import Sale, SaleDetail, Product


@api_view(["POST"])
def commit_data(request):
    try:
        with transaction.atomic():
            sale=Sale()
            sale.totalAmount=request.data["totalAmount"]
            sale.createBy_id = request.data["createBy"]
            sale.save()
        #add data to table sale detail
            saleId=Sale.objects.last()
            for i in range(len(request.data["sale"])):
                saleDetail=SaleDetail()
                saleDetail.sale_id=saleId.id
                saleDetail.product_id=request.data["sale"][i]["product"]
                saleDetail.qty=request.data["sale"][i]["qty"]
                saleDetail.price=request.data["sale"][i]["price"]
                saleDetail.total=saleDetail.qty * saleDetail.price
                saleDetail.save()
                product=Product.objects.get(pk=saleDetail.product_id)
                if product:
                    product.qtyInstock=product.qtyInstock - saleDetail.qty
                    product.save()
            transaction.commit()
            return Response({"message":"data Commited"})
    except Exception as ex:
        return Response({"Error":ex})