from django.db import models
class Clinic (models.Model):
    name= models.CharField (max_length=100,unique=True,verbose_name="اسم العياده")
    description=models.TextField(blank=True,verbose_name='وصف العياده')
    is_active=models.BooleanField(default=True,verbose_name="العياده متاحة")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

# Create your models here.
