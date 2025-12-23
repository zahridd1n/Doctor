from main.custom import CustomPagination, CustomResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from main.models import Registration
from main.serializer import RegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return CustomResponse.ok(
            data=serializer.data,
            message="Registration muvaffaqiyatli saqlandi"
        )


