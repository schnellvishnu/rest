from rest_framework.views import APIView
from rest_framework.response import Response
from reportapp.serializers import ProductionReportSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import ProductionReport
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

class ProductionOrderReport(APIView):
    def get(self, request):
        detailsObj = ProductionReport.objects.all()
        serializeObj = ProductionReportSerializer(detailsObj, many=True)
        return Response(serializeObj.data)

class ProductionOrderReportIndividual(APIView):
    def get(self, request, id):
        try:
            detailsObj = ProductionReport.objects.get(batch_number=id)
        except:
            return Response("Not found in databse")

        serializeObj = ProductionReportSerializer(detailsObj, data=request.data)
        if (serializeObj.is_valid()):
            return Response(serializeObj.data)

        return Response(serializeObj.errors)
