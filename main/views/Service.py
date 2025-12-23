from rest_framework.views import APIView
from main.custom import CustomResponse
from main.models import Service, ServicesDate, Portfolio
from main.serializer import ServiceSerializer, ServicesDateSerializer, PortfolioSerializer


class ServiceView(APIView):
    def get(self, request):
        services = Service.objects.all()
        services_date = ServicesDate.objects.last()

        data = {
            'services': ServiceSerializer(
                services, many=True, context={'request': request}
            ).data,
            'services_date': (
                ServicesDateSerializer(
                    services_date, context={'request': request}
                ).data if services_date else None
            ),
        }
        return CustomResponse.ok(data=data)


class PortfolioView(APIView):
    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(
            portfolios, many=True, context={'request': request}
        )
        return CustomResponse.ok(data=serializer.data)
