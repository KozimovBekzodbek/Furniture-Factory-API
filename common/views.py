from rest_framework import viewsets, permissions
from common import models
from common import serializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all() 
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get('status')
        queryset = models.Order.objects.all()
        if status:
            queryset = queryset.filter(status=status)
        return queryset

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = models.Worker.objects.all()
    serializer_class = serializers.WorkerSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

class RawMaterialViewSet(viewsets.ModelViewSet):
    queryset = models.RawMaterial.objects.all()
    serializer_class = serializers.RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

class FinishedProductViewSet(viewsets.ModelViewSet):
    queryset = models.FinishedProduct.objects.all()
    serializer_class = serializers.FinishedProductSerializer
    permission_classes = [permissions.IsAuthenticated]
