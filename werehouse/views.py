
from django.http import HttpResponse
from rest_framework import viewsets, status
from .models import warehouse
from .serializers import warehouseSerializer
from rest_framework.response import Response
# Create your views here.
def clpass(request):
    return HttpResponse("<h1>hello</h1>")

#class warehouse(viewsets.ModelViewSet):
 #   queryset = warehouse.objects.all()
  #  serializer_class = warehouseSerializer

class WarehouseSet(viewsets.ViewSet):
    def list (self, request):
        queryset = warehouse.objects.all()
        search = request.query_params.get('search')
        if search:
            queryset = queryset.filter(email__contains = search)
        serializer = warehouseSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = warehouseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)