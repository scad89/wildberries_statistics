from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/',
         views.RecordCardListView.as_view(), name='show_statistics'),
]
