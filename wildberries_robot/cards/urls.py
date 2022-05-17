from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/',
         views.GetStatiticsRetrieveAPIView.as_view(), name='questions'),
]
