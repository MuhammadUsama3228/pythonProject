from .serializers import ArticleSerializer
from .models import Article
from rest_framework import viewsets


class ArticleViewSets(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
