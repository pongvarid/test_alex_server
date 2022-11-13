from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend
from account.serializers import AccountSerializer, ReferrerSerializer, CommissionSerializer
from account.models import Account, Referrer, Commission
from company.models import Customer, OfficeCommission
from product.models import Product


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.order_by('pk')
    serializer_class = AccountSerializer
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class ReferrerViewSet(ModelViewSet):
    queryset = Referrer.objects.order_by('pk')
    serializer_class = ReferrerSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['master', 'child', ]
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class CommissionViewSet(ModelViewSet):
    queryset = Commission.objects.order_by('pk')
    serializer_class = CommissionSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['account', 'customer', 'product', 'by_my_child_commission', 'my_child_account' ]
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=request.data['customer'])
        product = Product.objects.get(pk=request.data['product'])
        of15 = product.price *15 /100
        of5 = of15 *5 /100
        of10 = of15 - of5
        calculateCommission = lambda price,percent: of10 * percent / 100
        storeCommission = lambda account, customer, product, percent, total, remark, byMyChild=False, myChild=None: Commission.objects.create(
            account=account,
            customer=customer,
            product=product,
            percent=percent,
            total=total,
            remark=remark,
            by_my_child_commission = byMyChild,
            my_child_account = myChild
        )
        #- 15% of product price to company
        officeCommission = OfficeCommission.objects.create(
            company=customer.sale.company,
            percent=5,
            total=of5,
            remark='15% of product price to company' + str(product.price) + ' from customer: ' + str(customer.name) + ' by sale: ' + str(customer.sale.first_name)+ str(customer.sale.last_name) + ' in product: ' + str(product.name)
        )
        #- Create My commission
        account = Account.objects.get(pk=int(request.data['sale']))
        myCommission = calculateCommission(product.price, account.tier.percent)
        storeCommission(account, customer, product, account.tier.percent, myCommission, 'My Commission of product: ' + product.name + '('+str(product.price)+'$)')

        #- Create My master commission
        masters = Referrer.objects.filter(child=account)
        for master in masters:
            masterCommission = calculateCommission(product.price, master.master.tier.percent)
            storeCommission(master.master, customer, product, master.master.tier.percent, masterCommission, 'By My Child Refferer Commission of product (by other refferer): ' + product.name + '('+str(product.price)+'$)', True, account)
         #- Create commission of my child
        childs = Referrer.objects.filter(master=account)
        for child in childs:
            childCommission = calculateCommission(product.price, child.child.tier.percent)
            storeCommission(account, customer, product, child.child.tier.percent, childCommission, 'By My Child Refferer Commission of product (by me): ' + product.name + '('+str(product.price)+'$)', True, child.child)

        return Response({
            'status': 'success',
            'message': 'Commission created successfully',
            'master' : len(masters),
            'child' : len(childs)
        })