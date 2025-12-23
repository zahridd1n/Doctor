from rest_framework.views import APIView
from main.custom import CustomResponse
from main.models import Banner
from main.serializer import BannerSerializer


class BannerView(APIView):
    def get(self, request):
        banner = Banner.objects.last()

        data = (
            BannerSerializer(banner, context={'request': request}).data
            if banner else None
        )

        return CustomResponse.ok(data=data)
