from rest_framework.response import Response
from order.models import *
from order.serializers import *
from product.models import *
from product.serializers import *
from rest_framework import generics
from rest_framework.views import APIView

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.using('order_db').all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.using('order_db').all()
    serializer_class = OrderSerializer


class GetProduct(APIView):
    def get(self, request):
        queryset = Product.objects.using('product_db').all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'message':'success','data':serializer.data})