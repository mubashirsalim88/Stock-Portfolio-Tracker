from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Unnamed Stock')
    symbol = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Assuming you have this field already
    daily_change = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # New field for daily change
    purchase_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
