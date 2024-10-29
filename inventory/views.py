from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .models import Product, Type, Price
from .serializers import ProductSerializer, TypeSerializer, PriceSerializer, ReduceQuantitySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def reduce_quantity(self, request, pk=None):
        product = self.get_object()
        serializer = ReduceQuantitySerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.update(product, serializer.validated_data) # Обновляем количество
                return Response({"status": "success", "message": "Количество успешно уменьшено"})
            except ValueError as e:
                return Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer