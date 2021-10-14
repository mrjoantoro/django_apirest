from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('token-auth/', obtain_auth_token, name='token_auth'),
]