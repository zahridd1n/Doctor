from rest_framework.generics import ListAPIView
from main.custom import CustomResponse
from main.models import FAQ
from main.serializer import FAQSerializer


class FAQView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return CustomResponse.ok(data=serializer.data)
