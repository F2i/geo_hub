from django.db import models


class GeoProduct(models.Model):
    OS_CHOICES = (
        ('Window', 'Window'),
        ('Linux', 'Linux'),
        ('MacOS', 'MacOS'),
    )
    title = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    os_platform = models.CharField(max_length=255, null=False, choices=OS_CHOICES)
    description = models.TextField(null=False)
