from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('learn-web-design/', views.learn_web_design, name="learn-web-design"),
    path('learn-software/', views.learn_software, name="learn-software"),
    path('learn-business/', views.learn_business, name="learn-business"),
    path('terms-of-use/', views.terms_of_use, name="terms-of-use"),
    path('privacy-policy/', views.privacy_policy, name="privacy-policy"),
    path('learn-archive/', views.learn_archive, name="learn-archive"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)