from django.urls import path
from main.views.Home import BannerView
from main.views.About import AdvantagesView, AboutView
from main.views.Service import ServiceView, PortfolioView
from main.views.Course import CourseView, CourseDetail, CourseRegisterView
from main.views.vebinar import VebinarView, VebinarDetail, VebinarRegisterView
from main.views.Contact import OurDataView, SocialsView, ContactsCreate
from main.views.faq import FAQView
from main.views.Shop import CategoryView, ProductListView, ProductDetailView
from main.views.Registration import RegistrationView
urlpatterns = [
    path('banner/', BannerView.as_view(), name='banner'),
    path('advantages/', AdvantagesView.as_view(), name='advantages'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServiceView.as_view(), name='service'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('course/', CourseView.as_view(), name='course'),
    path('vebinar/', VebinarView.as_view(), name='vebinar'),
    path('course/<int:id>/', CourseDetail.as_view(), name='course_detail'),
    path('course/register/', CourseRegisterView.as_view(), name='course_register'),
    path('vebinar/<int:id>/', VebinarDetail.as_view(), name='vebinar_detail'),
    path('vebinar/register/', VebinarRegisterView.as_view(), name='vebinar_register'),
    path('our-data/', OurDataView.as_view(), name='our_data'),
    path('socials/', SocialsView.as_view(), name='socials'),
    path('contacts/', ContactsCreate.as_view(), name='contacts'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('category/', CategoryView.as_view(), name='category'),
    path('product/', ProductListView.as_view(), name='product'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]