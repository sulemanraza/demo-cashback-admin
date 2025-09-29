from django.db import models
from apps.merchants.models import Merchant


class Promotion(models.Model):
    PROMOTION_TYPES = [
        ("coupon", "Coupon"),
        ("deal", "Deal / Automatic Offer"),
    ]

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="promotions")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    promotion_type = models.CharField(max_length=20, choices=PROMOTION_TYPES, default="deal")

    code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Only required if type is coupon"
    )

    discount = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="e.g. 10% OFF or 5€ Discount"
    )

    start_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.merchant.name} - {self.title} ({self.get_promotion_type_display()})"
