from django.urls import path
from .views import PatientListCreateAPIView, PatientDetailAPIView

urlpatterns = [
    # تم إضافة الفاصلة (,) المفقودة في نهاية السطر بالأسفل لإنهاء العنصر الأول في المصفوفة
    path('patients/', PatientListCreateAPIView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailAPIView.as_view(), name='patient-detail'),
]

