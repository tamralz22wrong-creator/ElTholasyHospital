from django.contrib import admin
from django.urls import path, include

# تأكد أن الكلمة تبدأ من أول السطر تماماً بدون أي مسافات قبلها
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('clinics/', include('clinics.urls')),
    path('patients/', include('patients.urls')),
    path('appointments/', include('appointments.urls')),
    path('doctors/', include('doctors.urls')),
]


