from rest_framework import serializers

from .models import Product, Type, Price


class ReduceQuantitySerializer(serializers.Serializer):
    amount = serializers.IntegerField()

    def update(self, instance, validated_data):
        amount = validated_data.get('amount')
        if amount is None:
            raise

        instance.reduce_quantity(amount)
        instance.save()
        return instance


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity', 'barcode', 'updated_at', 'product_type']