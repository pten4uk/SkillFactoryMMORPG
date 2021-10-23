from django.urls import path, include

from .views import CustomLogin

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('', include('allauth.urls')),
]