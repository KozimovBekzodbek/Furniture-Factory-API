from rest_framework import serializers
from common import models

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Worker
        fields = '__all__'

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RawMaterial
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class OrderWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderWorker
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    orderworker_set = OrderWorkerSerializer(many=True, read_only=True)

    class Meta:
        model = models.Order
        fields = '__all__'

class FinishedProductSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        queryset=models.Order.objects.filter(status='Tayyor')
    )

    def validate_order(self, value):
        if value.status != 'Tayyor':
            raise serializers.ValidationError("Faqat statusi 'Ready' bo‘lgan zakazlarga mahsulot bog‘lanadi.")
        return value

    order_name = serializers.CharField(source='order.name', read_only=True)
    order_price = serializers.FloatField(source='order.price', read_only=True)
    order_type = serializers.CharField(source='order.type', read_only=True)

    class Meta:
        model = models.FinishedProduct
        fields = ['id', 'order', 'order_name', 'order_price', 'order_type', 'quantity', 'image', 'workers']
