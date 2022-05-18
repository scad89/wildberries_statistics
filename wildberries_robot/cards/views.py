from rest_framework.response import Response
from rest_framework import permissions
from cards.services.getting_stats_services import getting_params
from rest_framework import generics, viewsets, status
from .models import UserArticle, RecordCard
from .serializers import ArticleSerializer, RecordCardSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """Add, show all and delete article"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = UserArticle.objects.all()


class RecordCardListView(generics.RetrieveAPIView):
    """Data for results in statistics"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = RecordCard.objects.all()
    serializer_class = RecordCardSerializer

    def get(self, request, *args, **kwargs):
        start_date, end_date, interval = getting_params(
            self.request.query_params)
        show_stat = RecordCard.objects.filter(id_article=kwargs['pk']).filter(
            record_time__range=[start_date, end_date]
        )[::interval]
        serializer = RecordCardSerializer(show_stat, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
