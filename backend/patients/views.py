
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Patient
from .serializers import PatientSerializer
from .permissions import IsStaffOrOwnPatient


class PatientListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStaffOrOwnPatient]

    def get(self, request):
        if request.user.is_staff:
            patients = Patient.objects.all()
        else:
            patients = Patient.objects.filter(user=request.user)

        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PatientDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStaffOrOwnPatient]

    def get_patient(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return None

    def get(self, request, pk):
        patient = self.get_patient(pk)

        if patient is None:
            return Response(
                {"detail": "Patient not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, patient)

        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = self.get_patient(pk)

        if patient is None:
            return Response(
                {"detail": "Patient not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, patient)

        serializer = PatientSerializer(patient, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        patient = self.get_patient(pk)

        if patient is None:
            return Response(
                {"detail": "Patient not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, patient)

        serializer = PatientSerializer(
            patient,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        patient = self.get_patient(pk)

        if patient is None:
            return Response(
                {"detail": "Patient not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, patient)

        patient.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




# Create your views here.
