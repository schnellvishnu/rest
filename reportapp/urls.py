from django.urls import path
from reportapp import views

urlpatterns = [
    path('ProductionOrderReport/', views.ProductionOrderReport.as_view()),
    path('ProductionOrderReportIndividual/<int:id>/', views.ProductionOrderReportIndividual.as_view()),
]