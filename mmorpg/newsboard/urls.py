from django.urls import path

from .views import *

app_name = 'newsboard'
urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('create/', PostCreate.as_view(), name='create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='update'),
]
