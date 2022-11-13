from rest_framework.viewsets import ModelViewSet
from company.serializers import CompanySerializer, TierSerializer, CustomerSerializer, OfficeCommissionSerializer
from company.models import Company, Tier, Customer, OfficeCommission
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.order_by('pk')
    serializer_class = CompanySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = []
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class TierViewSet(ModelViewSet):
    queryset = Tier.objects.order_by('pk')
    serializer_class = TierSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['company','level']
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class OfficeCommissionViewSet(ModelViewSet):
    queryset = OfficeCommission.objects.order_by('pk')
    serializer_class = OfficeCommissionSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['company' ]
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.order_by('pk')
    serializer_class = CustomerSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['sale__company','sale__tier__level']
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
