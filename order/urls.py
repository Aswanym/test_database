import imp
from django.urls import path,include
from order import views

urlpatterns = [
    path('order_list/', views.OrderList.as_view()),
    path('order_details/<int:pk>/', views.OrderDetail.as_view()),
    path('get_product/', views.GetProduct.as_view()),
]