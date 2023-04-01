from django.contrib import admin

# Register your models here.
from django.contrib import admin

from order.models import  OrderItem, update_order, wishitems

# Register your models here.
admin.site.register(wishitems)
admin.site.register(OrderItem)
admin.site.register(update_order)