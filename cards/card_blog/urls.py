from django.urls import path

from card_blog.views import CardViewSet


urlpatterns = [
    path('', CardViewSet.as_view()),
]