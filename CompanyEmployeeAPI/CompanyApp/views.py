from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import action

from .models import *
from .serializers import *

# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# companies/{{company_id}}/employees
    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        comp = Company.objects.get(pk=pk)
        emp = Employee.objects.filter(company=comp)

        emp_serializer = EmployeeSerializer(emp, many=True, context={'request': request})
        return Response(emp_serializer.data)



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer