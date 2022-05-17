from rest_framework.response import Response
from cards.services.getting_stats_services import getting_params
from rest_framework import generics
from .models import UserArticle, RecordCard
from rest_framework import viewsets
from .serializers import ArticleSerializer, RecordCardSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """Add, show all and delete article"""
    serializer_class = ArticleSerializer
    queryset = UserArticle.objects.all()


class RecordCardListView(generics.RetrieveAPIView):
    """Data for results in statistics"""
    queryset = RecordCard.objects.all()
    serializer_class = RecordCardSerializer

    def get(self, request, *args, **kwargs):
        start_date, end_date, interval = getting_params(
            self.request.query_params)
        show_stat = RecordCard.objects.filter(id_article=kwargs['pk']).filter(
            record_time__range=[start_date, end_date]
        )[::interval]
        serializer = RecordCardSerializer(show_stat, many=True)
        return Response(serializer.data)
