from rest_framework import serializers
from .models import Patient # تأكد من أن اسم الموديل Patient

class PatientSerializer(serializers.ModelSerializer):
    # تم تصحيح الحقل هنا إلى IntegerField لأن DRF لا يحتوي على PositiveIntegerField
    age = serializers.IntegerField(min_value=1, max_value=130)

    class Meta:
        model = Patient
        fields = '__all__'
