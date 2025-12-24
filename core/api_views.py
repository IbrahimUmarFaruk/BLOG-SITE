from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

# API View to List all Articles
class ArticleListAPI(generics.ListAPIView):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer

# API View to Retrieve a Single Article
class ArticleDetailAPI(generics.RetrieveAPIView):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer
    lookup_field = 'int:pk' # We will look up articles by their slug [cite: 452]