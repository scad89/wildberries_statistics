from rest_framework import serializers
from .models import UserArticle, RecordCard


class ArticleSerializer(serializers.ModelSerializer):
    """Add, show all and delete article"""
    class Meta:
        model = UserArticle
        fields = "__all__"


class RecordCardSerializer(serializers.ModelSerializer):
    """Data for results in statistics"""
    id_article = serializers.SlugRelatedField(
        slug_field='article', read_only=True)

    class Meta:
        model = RecordCard
        fields = "__all__"
