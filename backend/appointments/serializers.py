from rest_framework import serializers
from .models import Appointment
from django.utils import timezone
from datetime import datetime

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        doctor = data.get('doctor')
        appointment_date = data.get('appointment_date')

        # ------------------------------------------------------------------
        # الشرط الأول: منع حجز نفس الموعد لنفس الطبيب (تضارب المواعيد)
        # ------------------------------------------------------------------
        # يبحث في قاعدة البيانات عن أي حجز نشط لنفس الدكتور وفي نفس الوقت تمامًا
        exists = Appointment.objects.filter(
            doctor=doctor, 
            appointment_date=appointment_date
        ).exists()
        
        if exists:
            raise serializers.ValidationError(
                {"appointment_date": "عذرًا، هذا الوقت محجوز مسبقًا مع هذا الطبيب. يرجى اختيار وقت آخر."}
            )

        # ------------------------------------------------------------------
        # الشرط الثاني: حد أقصى 20 حجزًا في اليوم للمستشفى بالكامل
        # ------------------------------------------------------------------
        # استخراج تاريخ اليوم فقط (بدون الساعات والدقائق)
        if appointment_date:
            # إذا كان التاريخ قادمًا كـ string نقوم بتحويله، أو نأخذ التاريخ مباشرة لو كان datetime object
            if isinstance(appointment_date, str):
                booking_day = datetime.strptime(appointment_date, "%Y-%m-%dT%H:%M:%S").date()
            else:
                booking_day = appointment_date.date()

            # حساب عدد الحجوزات المسجلة في هذا اليوم بالتحديد
            daily_count = Appointment.objects.filter(
                appointment_date__date=booking_day
            ).count()

            if daily_count >= 20:
                raise serializers.ValidationError(
                    {"appointment_date": "عذرًا، اكتمل الحد الأقصى للمواعيد المتاحة لهذا اليوم (20 حجزًا). يرجى اختيار يوم آخر."}
                )

        return data
