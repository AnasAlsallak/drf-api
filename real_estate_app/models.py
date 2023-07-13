from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class RealEstate (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='static/', blank=True)
    photo_1 = models.ImageField(upload_to='static/', blank=True)
    photo_2 = models.ImageField(upload_to='static/', blank=True)
    photo_3 = models.ImageField(upload_to='static/', blank=True)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

