from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from main.custom import CustomResponse
from main.models import Courses, CourseRegister
from main.serializer import CourseSerializer, CourseRegisterSerializer


class CourseView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Courses.objects.prefetch_related("photos")

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return CustomResponse.ok(data=serializer.data)


class CourseDetail(RetrieveAPIView):
    serializer_class = CourseSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Courses.objects.prefetch_related("photos")

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return CustomResponse.ok(data=serializer.data)


class CourseRegisterView(generics.CreateAPIView):
    queryset = CourseRegister.objects.all()
    serializer_class = CourseRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return CustomResponse.ok(
            data=serializer.data,
            message="Course register muvaffaqiyatli saqlandi"
        )
