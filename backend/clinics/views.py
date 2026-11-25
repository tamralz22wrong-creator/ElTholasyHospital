from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Clinic
from .serializers import ClinicSerializer

class ClinicApiView(APIView):

    def get(self, request):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# كلاس منفصل ومخصص للعمليات التي تحتاج مُعرف العيادة (مثل الحذف أو جلب عيادة واحدة)
class ClinicDetailApiView(APIView):

    def delete(self, request, pk):
        try:
            clinic = Clinic.objects.get(pk=pk)
        except Clinic.DoesNotExist:
            return Response({"error": "Clinic not found"}, status=status.HTTP_404_NOT_FOUND)
        
        clinic.delete()
        return Response({"message": "Clinic deleted successfully"}, status=status.HTTP_200_OK)







# Create your views here.
