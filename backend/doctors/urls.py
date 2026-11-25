from django.urls import path
from .views import DoctorListApiView, DoctorDetailAPIView

urlpatterns = [
    # 1. تم حذف الشرطة المائلة من البداية ليكون المسار فارغاً تماماً ''
    path('', DoctorListApiView.as_view(), name='doctor-list-create'),

    # 2. تم حذف الشرطة المائلة من بداية مسار الـ pk ليبدأ بـ <int:pk> مباشرة
    path('<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),
]
