from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class OfficeCommission(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    percent = models.FloatField(default=0)
    total = models.FloatField(default=0)
    remark = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.percent)

class Tier(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    level = models.IntegerField(default=1)
    percent = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.name + ' ( level: '+ str(self.level)+')'

class Customer(models.Model):
    sale = models.ForeignKey('account.Account', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def company(self):
        try:
            return self.sale.company
        except:
            return "-"