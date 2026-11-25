from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    # تم تحديث الأسماء لتطابق full_name و specialization و is_available
    list_display = ('full_name', 'specialization', 'phone', 'is_available')
    list_filter = ('specialization', 'is_available')
    search_fields = ('full_name', 'specialization')

