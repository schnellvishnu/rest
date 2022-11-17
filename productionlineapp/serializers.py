from productionlineapp.models import ManufacturingLocations,RegisteredSystem,Task
from rest_framework import serializers
# from apps.productionlineapp.models import ManufacturingLocations,RegisteredSystem, Task

# from .masterapp.models import ProductionOrder
# from apps.accounts.serializers import UserSerializer
class ManufacturingLocSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ManufacturingLocations
        fields = "__all__"
        # read_only_fields = ['created_by']
# ----------------------------------------------------------------
class RegisterSystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredSystem
        fields = "__all__"
#----------------------------------------------------------------------
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model =Task
        fields = "__all__"