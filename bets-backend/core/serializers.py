from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Bet, BetOption, BetParticipant

class BetOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetOption
        fields = ('id', 'title')

class BetSerializer(serializers.ModelSerializer):
    options = BetOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Bet
        fields = ('id', 'title', 'description', 'creator', 'created_at', 'updated_at', 'is_public', 'options')

class BetParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetParticipant
        fields = ('id', 'user', 'bet', 'chosen_option', 'amount', 'created_at', 'updated_at')

class BetCreateSerializer(serializers.ModelSerializer):
    options = BetOptionSerializer(many=True, required=False)

    class Meta:
        model = Bet
        fields = ('id', 'title', 'description', 'creator', 'is_public', 'options')
    
    def validate_options(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('At least two bet options are required.')
        return value

    def create(self, validated_data):
        options_data = validated_data.pop('options', [])
        bet = Bet.objects.create(**validated_data)

        for option_data in options_data:
            BetOption.objects.create(bet=bet, **option_data)

        return bet
