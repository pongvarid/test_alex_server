from django.contrib import admin
from django.contrib.auth.hashers import check_password, make_password

from account.models import Account, Commission, Referrer
from company.models import Customer


# Register your models here.
class ReferrerMyMasterInline(admin.TabularInline):
    model = Referrer
    extra = 1
    fk_name = 'child'
    verbose_name = "Referrer Master"
    verbose_name_plural = "Referrer Master"

class ReferrerMyChildInline(admin.TabularInline):
    model = Referrer
    fk_name = 'master'
    extra = 1
    verbose_name = "Referrer Child"
    verbose_name_plural = "Referrer Child"

class CustomerInline(admin.TabularInline):
    model = Customer
    fk_name = 'sale'
    extra = 1

class CommissionInline(admin.TabularInline):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    model = Commission
    fk_name = 'account'
    extra = 1
class AccountAdmin(admin.ModelAdmin):
    inlines = [ReferrerMyChildInline, ReferrerMyMasterInline, CustomerInline, CommissionInline]
    list_display = ('first_name', 'last_name', 'email', 'level','company', 'created_at', 'updated_at')
    list_filter = ('company','tier', 'created_at', 'updated_at', 'is_active')
    search_fields = ('company__name','tier__level','first_name', 'last_name', 'email','created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        try:
            user_database = Account.objects.get(pk=obj.pk)
        except Exception:
            user_database = None
        if user_database is None \
                or not (check_password(form.data['password'], user_database.password)
                        or user_database.password == form.data['password']):
            obj.password = make_password(obj.password)
        else:
            obj.password = user_database.password
        super().save_model(request, obj, form, change)

admin.site.register(Account, AccountAdmin)

class CommissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_display = ('account', 'percent', 'total','by_my_child_commission','my_child_account','company', 'created_at', 'updated_at')
    list_filter = ('account__company','by_my_child_commission','created_at', 'updated_at')
    search_fields = ('account__first_name', 'percent','total','created_at', 'updated_at')
admin.site.register(Commission, CommissionAdmin)
