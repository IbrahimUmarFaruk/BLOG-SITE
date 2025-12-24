from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # We choose which fields to share in the API [cite: 442]
        fields = ['id', 'title', 'image', 'body', 'date', 'author']