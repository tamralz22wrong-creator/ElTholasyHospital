from django.db import models

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'مجدول'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    ]

    patient = models.ForeignKey(
        'patients.Patient',
        on_delete=models.PROTECT,
        related_name='appointments',
    )

    doctor = models.ForeignKey(
        'doctors.Doctor',
        on_delete=models.PROTECT,
        related_name='appointments',
    )

    appointment_date = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled',
    )

    reason = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.appointment_date}"


    
    
# Create your models here.
