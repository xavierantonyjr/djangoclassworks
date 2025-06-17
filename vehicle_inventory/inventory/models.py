from django.db import models

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='vehicle_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.year})"
