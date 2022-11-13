from rest_framework.serializers import ModelSerializer, SerializerMethodField
from account.models import Account, Referrer, Commission


class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        exclude = ('password', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', 'last_login', 'date_joined', 'created_at', 'updated_at', )


class ReferrerSerializer(ModelSerializer):
    master_data = SerializerMethodField(read_only=True)
    child_data = SerializerMethodField(read_only=True)
    class Meta:
        model = Referrer
        fields = '__all__'
    def get_master_data(self, obj):
        try:
            return obj.master.first_name + ' ' + obj.master.last_name + ' (Level:' + str(obj.master.tier.level) + ', Percent:' + str(obj.master.tier.percent) + '%)'
        except:
            return None
    def get_child_data(self, obj):
        try:
            return obj.child.first_name + ' ' + obj.child.last_name + ' (Level:' + str(obj.child.tier.level) + ', Percent:' + str(obj.child.tier.percent) + '%)'
        except:
            return None


class CommissionSerializer(ModelSerializer):
    product_data = SerializerMethodField(read_only=True)
    account_data = SerializerMethodField(read_only=True)
    customer_data = SerializerMethodField(read_only=True)
    my_child_account_data = SerializerMethodField(read_only=True)
    class Meta:
        model = Commission
        fields = '__all__'

    def get_product_data(self, obj):
        try:
            return obj.product.name + ' (' + str(obj.product.price) + '$)'
        except:
            return None

    def get_account_data(self, obj):
        try:
            return obj.account.first_name + ' ' + obj.account.last_name
        except:
            return None

    def get_customer_data(self, obj):
        try:
            return obj.customer.name
        except:
            return None

    def get_my_child_account_data(self, obj):
        try:
            return obj.my_child_account.first_name + ' ' + obj.my_child_account.last_name + ' (Level:' + str(obj.my_child_account.tier.level) + ', Percent:' + str(obj.my_child_account.tier.percent) + '%)'
        except:
            return None
