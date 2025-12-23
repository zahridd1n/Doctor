from rest_framework.views import APIView
from rest_framework import generics
from main.custom import CustomResponse
from main.models import Contacts, OurData, Socials
from main.serializer import ContactsSerializer, OurDataSerializer, SocialsSerializer


class OurDataView(APIView):
    def get(self, request):
        our_data = OurData.objects.last()

        data = (
            OurDataSerializer(our_data, context={'request': request}).data
            if our_data else None
        )

        return CustomResponse.ok(data=data)


class SocialsView(APIView):
    def get(self, request):
        socials = Socials.objects.all()
        serializer = SocialsSerializer(
            socials, many=True, context={'request': request}
        )
        return CustomResponse.ok(data=serializer.data)


class ContactsCreate(generics.CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return CustomResponse.ok(
            data=serializer.data,
            message="Contact muvaffaqiyatli saqlandi"
        )
