from rest_framework import serializers
from .models import UserArticle


class AddArticleSerializer(serializers.ModelSerializer):
    """Add article"""

    class Meta:
        model = UserArticle
        fields = ['article']


class ArticleSerializer(serializers.ModelSerializer):
    """Show all articles"""

    class Meta:
        model = UserArticle
        exclude = ['unvisible']


class DeleteArticleSerializer(serializers.ModelSerializer):
    """Delete articles"""

    class Meta:
        model = UserArticle
        fields = ['unvisible']
