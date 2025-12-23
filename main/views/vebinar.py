from rest_framework import generics
from main.custom import CustomResponse
from main.models import Vebinar, VebinarRegister
from main.serializer import VebinarSerializer, VebinarRegisterSerializer


class VebinarView(generics.ListAPIView):
    queryset = Vebinar.objects.all()
    serializer_class = VebinarSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return CustomResponse.ok(data=serializer.data)


class VebinarDetail(generics.RetrieveAPIView):
    queryset = Vebinar.objects.all()
    serializer_class = VebinarSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return CustomResponse.ok(data=serializer.data)


class VebinarRegisterView(generics.CreateAPIView):
    queryset = VebinarRegister.objects.all()
    serializer_class = VebinarRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return CustomResponse.ok(
            data=serializer.data,
            message="Vebinar register muvaffaqiyatli saqlandi"
        )
