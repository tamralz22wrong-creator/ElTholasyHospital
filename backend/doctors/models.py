from django.db import models
from django.conf import settings # 1. استدعاء مكتبة الإعدادات لربط المستخدم المخصص

class Doctor(models.Model):
    # 2. ربط الطبيب بالمستخدم المخصص بأمان التام لتفادي أخطاء التضارب
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    license_number = models.CharField(max_length=50, unique=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    clinic_address = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name




# Create your models here.
