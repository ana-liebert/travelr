from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="first name")
    last_name = models.CharField(max_length=100, default="last name")
    profile_pic = models.CharField(max_length=500, default="http")
    city = models.CharField(max_length=60)
    join_date = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.user.username


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    grid_img = models.CharField(max_length=250, default="http")

    def __str__(self):
        return self.name

CATEGORY_CHOICES = (
    ("food", "Food"),
    ("bar", "Bar"),
    ("arts", "Arts"),
    ("nightlife", "Nightlife"),
    ("culture", "Culture"),
    ("sights", "Sights"),
    ("cafes", "Cafes"),
    ("shops", "Shops"),
    ("outdoors", "Outdoors"),
)

class Guide(models.Model):
    title = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="cities")
    country = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='none')
    image = models.CharField(max_length=200, null=True)
    image2 = models.CharField(max_length=200, null=True, blank=True)
    image3 = models.CharField(max_length=200, null=True, blank=True)
    image4 = models.CharField(max_length=200, null=True, blank=True)
    image5 = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")

    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return self.title