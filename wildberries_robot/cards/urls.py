from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.GetArticleListView.as_view(), name='articles'),
    path('add_article/', views.NewArticleCreateAPIView.as_view(), name='add_article'),
    path("article/<int:pk>/", views.DeleteArticleRetrieveUpdateApiView.as_view(),
         name='delete_article'),
]
