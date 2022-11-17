from django.contrib import admin
from masterapp.models import Company,Customers,Locations,Product,ShipPO,ProductionOrder,BarCodeType,SnProvider,Stock
# Register your models here.
admin.site.register(Company)
admin.site.register(Customers)
admin.site.register(Locations)
admin.site.register(Product)
admin.site.register(ShipPO)
admin.site.register(ProductionOrder)
admin.site.register(BarCodeType)
admin.site.register(SnProvider)
admin.site.register(Stock)