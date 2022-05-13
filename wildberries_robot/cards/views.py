from rest_framework import generics
from .models import UserArticle, RecordCard
from rest_framework import viewsets
from .serializers import ArticleSerializer, RecordCardSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """Add, show all and delete article"""
    serializer_class = ArticleSerializer
    queryset = UserArticle.objects.all()


class RecordCardListView(viewsets.ModelViewSet):
    """Вывод списка вопросов"""
    queryset = RecordCard.objects.all()
    serializer_class = RecordCardSerializer
