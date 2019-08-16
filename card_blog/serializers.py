from rest_framework import serializers

from card_blog.models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card

        fields = (
            'id',
            'answer',
            'created_dt',
            'question',
        )
