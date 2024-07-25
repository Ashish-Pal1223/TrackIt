from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class action(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null= True)

    def __str__(self):
        return f"{self.title} ({self.rating})"

class Romance(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null= True)

    def __str__(self):
        return f"{self.title} ({self.rating})"
    

class psychological(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null= True)

    def __str__(self):
        return f"{self.title} ({self.rating})"
