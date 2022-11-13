from rest_framework.viewsets import ModelViewSet
from product.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

