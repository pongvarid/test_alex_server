from rest_framework.serializers import ModelSerializer,SerializerMethodField
from product.models import Product


class ProductSerializer(ModelSerializer):
    product_data = SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

    def get_product_data(self, obj):
        return obj.name + ' (' + str(obj.price) + '$)'
