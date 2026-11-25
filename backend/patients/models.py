from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class Patient(models.Model):
    name =models.CharField(max_length=100)
    phone =models.CharField(max_length=15)
    medical_condition =models.TextField()
    age =models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(130)])
    email =models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

# Create your models here.
