from masterapp.models import Company,Customers,Locations, Product, ProductionOrder, ShipPO,BarCodeType,SnProvider, Stock
from rest_framework import serializers
class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Company
        fields = ["id","company_name","zip","state","created_by","gln","address"]
class CustomersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Customers
        fields =["id","name","company_prefix","company_gln","address","zip","created_by"]
class LocationSerializer(serializers.ModelSerializer):
    # customer_id = CustomersSerializer()
    customer_id = serializers.SlugRelatedField(slug_field='name',read_only=True)

    class Meta:
        model =Locations
        fields = ['id','name','customer_id','address','zip','state','loc_gln','created_by']
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ["id","name","gtin_number","imn","description","created_by"]
class ShipPOSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShipPO
        fields = "__all__"
class ProductionOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductionOrder
        fields = "__all__"
class BarCodeTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =BarCodeType
        fields = "__all__"
class SnProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =SnProvider
        fields = "__all__"
class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Stock
        fields = ["id","productionorder_num","product_name","created_by","batch_num","stock_quantity","shipped"]