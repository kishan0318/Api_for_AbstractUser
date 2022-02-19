from django.urls import path
from .views import *


app_name = 'app1'

urlpatterns=[

    path("register",RegisterAPIView.as_view(),name='register'),
    path("signup",SignupAPIView.as_view(),name='register'),
    path("login",LoginAPIView.as_view(),name='Login'),
    path("update",UpdateAPIView.as_view(),name='update'),
    path("Update/<int:pk>",UpdateAPIView2.as_view(),name='update2'),
    path("delete",DeleteAPIView1.as_view(),name='delete'),
    path("delete1/<int:pk>",DeleteAPIView2.as_view(),name='delete1'),
 





]