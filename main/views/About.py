from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from main.custom import CustomResponse
from main.models import Advantages, About
from main.serializer import AboutSerializer, AdvantagesSerializer


class AdvantagesView(ListAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return CustomResponse.ok(data=serializer.data)


class AboutView(APIView):
    def get(self, request):
        about = About.objects.last()
        data = (
            AboutSerializer(about, context={'request': request}).data
            if about else None
        )
        return CustomResponse.ok(data=data)
