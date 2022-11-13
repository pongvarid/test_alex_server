from django.contrib import admin

from company.models import Company, Tier, OfficeCommission, Customer


class TierInline(admin.TabularInline):
    model = Tier
    extra = 1

class OfficeCommissionInline(admin.TabularInline):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    model = OfficeCommission
    extra = 1

class CompanyAdmin(admin.ModelAdmin):
    inlines = [TierInline, OfficeCommissionInline]
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name','created_at', 'updated_at')
admin.site.register(Company,CompanyAdmin)

class TierAdmin(admin.ModelAdmin):
    list_display = ('company', 'level', 'percent', 'created_at', 'updated_at')
    list_filter = ('company', 'level', 'percent', 'created_at', 'updated_at')
    search_fields = ('company__name', 'level', 'percent','created_at', 'updated_at')
admin.site.register(Tier, TierAdmin)

class OfficeCommissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_display = ('company', 'percent', 'total', 'created_at', 'updated_at')
    list_filter = ('company', 'percent', 'total','created_at', 'updated_at')
    search_fields = ('company__name', 'percent','total','created_at', 'updated_at')
admin.site.register(OfficeCommission, OfficeCommissionAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ( 'name','phone', 'email', 'address', 'sale', 'company','is_active', 'created_at', 'updated_at')
    list_filter = ('sale', 'sale__company', 'is_active', 'created_at', 'updated_at')
    search_fields = ('sale__first_name', 'sale__company__name', 'phone', 'email', 'address', 'is_active','created_at', 'updated_at')
admin.site.register(Customer,CustomerAdmin )