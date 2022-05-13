from rest_framework import serializers
from .models import UserArticle, RecordCard


class ArticleSerializer(serializers.ModelSerializer):
    """Add, show all and delete article"""
    class Meta:
        model = UserArticle
        fields = "__all__"


class RecordCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordCard
        fields = "__all__"
