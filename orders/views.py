from django.shortcuts import render
from rest_framework import generics
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework.throttling import UserRateThrottle

from orders.models import Order
from orders.serializers import OrderSerializer, OrderCreateSerializer


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        if self.request.query_params.get("id"):
            return Order.objects.all().filter(id=self.request.query_params.get("id"))
        else:
            return Order.objects.all()

class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return Order.objects.all()


class OrderUpdate(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]


class OrderDelete(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]