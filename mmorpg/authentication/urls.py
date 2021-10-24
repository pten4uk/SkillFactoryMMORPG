from django.urls import path, include

from .views import CustomLogin, CustomSignup

urlpatterns = [
    path('', include('allauth.urls')),
]