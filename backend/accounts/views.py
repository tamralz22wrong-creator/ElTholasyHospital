from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User

# تم تعديل حرف s الصغير إلى S كبير ليطابق ملف الـ urls تماماً
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
