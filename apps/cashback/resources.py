from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import CashbackTransaction
from apps.users.models import CustomUser
from apps.merchants.models import Merchant


class CashbackTransactionResource(resources.ModelResource):
    user = fields.Field(
        column_name="user",
        attribute="user",
        widget=ForeignKeyWidget(CustomUser, "username")  # match by username
    )
    merchant = fields.Field(
        column_name="merchant",
        attribute="merchant",
        widget=ForeignKeyWidget(Merchant, "name")  # match by merchant name
    )

    class Meta:
        model = CashbackTransaction
        fields = (
            "id",
            "user",
            "merchant",
            "order_id",
            "amount",
            "cashback_amount",
            "status",
        )
        export_order = fields
