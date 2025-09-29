from import_export import resources, fields
from .models import Merchant


class MerchantResource(resources.ModelResource):
    class Meta:
        model = Merchant
        fields = (
            "id",
            "name",
            "slug",
            "network",
            "network_id",
            "tracking_url",
            "commission_rate",
            "is_featured",
            "is_active",
            "created_at",
        )
        export_order = (
            "id",
            "name",
            "slug",
            "network",
            "network_id",
            "tracking_url",
            "commission_rate",
            "is_featured",
            "is_active",
            "created_at",
        )
