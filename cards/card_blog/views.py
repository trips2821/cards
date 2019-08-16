from rest_framework import generics

from card_blog.models import Card
from card_blog.serializers import CardSerializer

class CardViewSet(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

