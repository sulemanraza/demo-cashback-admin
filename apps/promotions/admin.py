from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Promotion
from .resources import PromotionResource


@admin.register(Promotion)
class PromotionAdmin(ImportExportModelAdmin):
    resource_class = PromotionResource

    list_display = (
        "title",
        "merchant",
        "promotion_type",
        "code",
        "discount",
        "expiry_date",
        "is_active",
        "is_featured",
    )
    list_filter = ("promotion_type", "is_active", "is_featured", "merchant", "expiry_date")
    search_fields = ("title", "merchant__name", "code")
    date_hierarchy = "expiry_date"

    actions = ["activate_promotions", "deactivate_promotions"]

    def activate_promotions(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} promotions activated.")

    def deactivate_promotions(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} promotions deactivated.")

    activate_promotions.short_description = "Mark selected promotions as active"
    deactivate_promotions.short_description = "Mark selected promotions as inactive"
