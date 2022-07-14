from django.contrib import admin

from order.models import Order, SecondOrder

# Register your models here.
admin.site.register(Order)
admin.site.register(SecondOrder)