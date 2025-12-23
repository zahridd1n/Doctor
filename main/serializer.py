from rest_framework import serializers
from main.models import Banner, Advantages, About, Service, ServicesDate, Portfolio, FAQ, Contacts, OurData, Socials, Registration, Vebinar, VebinarRegister, Courses, CoursePhotos, CourseRegister, Category, Product


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServicesDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesDate
        fields = ['date',]


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class CoursePhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePhotos
        fields = ["id", "image"]

class CourseSerializer(serializers.ModelSerializer):
    photos = CoursePhotosSerializer(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = "__all__"


class VebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vebinar
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class OurDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurData
        fields = '__all__'

class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class CourseRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegister
        fields = '__all__'


class VebinarRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = VebinarRegister
        fields = '__all__'