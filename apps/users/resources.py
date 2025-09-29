from import_export import resources
from .models import CustomUser


class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "wallet_balance",
            "is_active",
            "date_joined",
        )
        export_order = (
            "id",
            "username",
            "email",
            "wallet_balance",
            "is_active",
            "date_joined",
        )
