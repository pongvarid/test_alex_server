from rest_framework.serializers import ModelSerializer, SerializerMethodField
from company.models import Company, Tier, Customer, OfficeCommission


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class TierSerializer(ModelSerializer):

    class Meta:
        model = Tier
        fields = '__all__'

class OfficeCommissionSerializer(ModelSerializer):

    class Meta:
        model = OfficeCommission
        fields = '__all__'

class CustomerSerializer(ModelSerializer):
    sale_data = SerializerMethodField(read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'

    def get_sale_data(self, obj):
        try:
            return obj.sale.first_name +' '+obj.sale.last_name+ ' (Level:' + str(obj.sale.tier.level) + ', Percent:' + str(obj.sale.tier.percent) + '%)'
        except:
            return None
