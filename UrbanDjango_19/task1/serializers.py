from rest_framework import serializers
from task1.models import Buyer, Game, Review


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'name', 'balance']

class GameSerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer(read_only=True)  # Вложенный сериализатор

    class Meta:
        model = Game
        fields = ['id', 'title', 'cost', 'size', 'description', 'age_limited', 'buyer']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'game', 'author', 'rating', 'comment', 'created_at']
