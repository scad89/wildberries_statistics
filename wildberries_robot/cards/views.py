from rest_framework import generics
from .models import UserArticle
from .serializers import AddArticleSerializer, ArticleSerializer, DeleteArticleSerializer


class NewArticleCreateAPIView(generics.CreateAPIView):
    """Add new article"""
    queryset = UserArticle.objects.filter(unvisible=False)
    serializer_class = AddArticleSerializer


class GetArticleListView(generics.ListAPIView):
    """Show all article"""
    queryset = UserArticle.objects.filter(unvisible=False)
    serializer_class = ArticleSerializer


class DeleteArticleRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    """Delete articles"""
    queryset = UserArticle.objects.filter(unvisible=False)
    serializer_class = DeleteArticleSerializer
