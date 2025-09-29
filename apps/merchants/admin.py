from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Merchant
from .resources import MerchantResource

@admin.register(Merchant)
class MerchantAdmin(ImportExportModelAdmin):
    resource_class = MerchantResource
    list_display = ("name", "network", "network_id", "is_featured", "is_active", "created_at")
    list_filter = ("network", "is_featured", "is_active", "created_at")
    search_fields = ("name", "network", "network_id")
    prepopulated_fields = {"slug": ("name",)}

    actions = ["make_featured", "make_inactive"]

    def make_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f"{updated} merchants marked as featured.")

    def make_inactive(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} merchants marked as inactive.")

    make_featured.short_description = "Mark selected merchants as featured"
    make_inactive.short_description = "Mark selected merchants as inactive"
