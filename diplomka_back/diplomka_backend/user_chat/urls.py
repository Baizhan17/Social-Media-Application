from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .import api
urlpatterns = [
    path('',api.conv_list,name='conv_list'),
    path('<uuid:pk>/',api.conv_message,name='conv_message'),
    path('<uuid:pk>/send/',api.send_conv_message,name='send_conv_message'),
    path('<uuid:user_pk>/get-create/',api.conv_get_create,name='conv_get_create'),
    
]