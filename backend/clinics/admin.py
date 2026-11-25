from django.contrib import admin
from .models import Clinic
@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display=('name','is_active','created_at')
    list_filter=('is_active',)
    search_fields=('name',)
# Register your models here.
