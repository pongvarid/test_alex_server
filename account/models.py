from django.db import models
from django.contrib.auth.models import AbstractUser
from company.models import Company, Tier, Customer
from product.models import Product


class Account(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def level(self):
        try:
            return self.tier.level
        except:
            return "-"


class Referrer(models.Model):
    master = models.ForeignKey(Account, on_delete=models.CASCADE)
    child = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='child')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.master.first_name

class Commission(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    by_my_child_commission = models.BooleanField(default=False)
    my_child_account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name='my_child_account')
    percent = models.FloatField(default=0)
    total = models.FloatField(default=0)
    remark = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
           return str(self.account.id) + ' ' + str(self.customer.name) + ' ' + str(self.product.name)
        except:
             return str(self.id)

    def company(self):
        try:
            return self.account.company
        except:
            return "-"



