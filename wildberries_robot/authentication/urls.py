from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.RegisterGenericAPIView.as_view(), name='registration'),
    path('login/', views.LoginGenericAPIView.as_view(), name='login'),
    path('logout/', views.LogoutGenericAPIView.as_view(), name='logout'),

]
