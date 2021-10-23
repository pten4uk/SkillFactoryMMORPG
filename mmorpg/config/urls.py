from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsboard/', include('newsboard.urls')),
    path('auth/', include('authentication.urls')),
]
