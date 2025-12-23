from rest_framework.generics import ListAPIView, RetrieveAPIView
from main.custom import CustomResponse
from main.models import Category, Product
from main.serializer import CategorySerializer, ProductSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return CustomResponse.ok(data=serializer.data)


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return CustomResponse.ok(data=serializer.data)


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return CustomResponse.ok(data=serializer.data)
