from django.urls import path
from .views import ClinicApiView

urlpatterns = [
    # 1. جعل المسار فارغًا لأن 'clinics/' مبرمجة بالفعل في الملف الرئيسي config/urls.py
    path('', ClinicApiView.as_view(), name='get-clinics'),
    
    # 2. تصحيح صياغة مستقبل المعرّف (ID) ليكون بالصيغة القياسية لدجانجو <int:pk>
    path('<int:pk>/', ClinicApiView.as_view(), name='clinic-detail'),
]

