from django.db import models

from company.models import Company


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    price = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name