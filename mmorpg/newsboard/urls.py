from django.urls import path

from .views import PostList

app_name = 'newsboard'
urlpatterns = [
    path('', PostList.as_view(), name='home'),
]
