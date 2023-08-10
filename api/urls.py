from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSets


router = routers.DefaultRouter()
router.register(r'api', ArticleViewSets)

urlpatterns = [
    path('', include(router.urls)),
]