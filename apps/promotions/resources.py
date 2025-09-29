from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Promotion
from apps.merchants.models import Merchant


class PromotionResource(resources.ModelResource):
    merchant = fields.Field(
        column_name="merchant",
        attribute="merchant",
        widget=ForeignKeyWidget(Merchant, "name")  # match by merchant name
    )

    class Meta:
        model = Promotion
        fields = (
            "id",
            "merchant",
            "title",
            "description",
            "promotion_type",
            "code",
            "discount",
            "start_date",
            "expiry_date",
            "is_active",
            "is_featured",
            "created_at",
        )
        export_order = (
            "id",
            "merchant",
            "title",
            "description",
            "promotion_type",
            "code",
            "discount",
            "start_date",
            "expiry_date",
            "is_active",
            "is_featured",
            "created_at",
        )
