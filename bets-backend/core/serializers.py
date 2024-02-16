from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Bet, BetOption, BetParticipant

class BetOptionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)  # Include id field for updates

    class Meta:
        model = BetOption
        fields = ('id', 'title')

class BetSerializer(serializers.ModelSerializer):
    options = BetOptionSerializer(many=True, read_only=False)

    class Meta:
        model = Bet
        fields = ('id', 'title', 'description', 'is_public', 'options')
        read_only_fields = ('creator',)

    def validate_options(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('At least two bet options are required.')
        
        # make sure options are unique
        titles = [option['title'] for option in value]
        if len(set(titles)) != len(titles):
            raise serializers.ValidationError('Bet option titles must be unique.')
        return value

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.save()

        # update options
        options_data = validated_data.get('options', [])
        option_ids = []
        for option_data in options_data:
            option_id = option_data.get('id')
            if option_id:
                option = BetOption.objects.get(pk=option_id, bet=instance)
                option.title = option_data.get('title', option.title)
                option_ids.append(option_id)
                option.save()
            else:
                option = BetOption.objects.create(bet=instance, **option_data)
                option_ids.append(option.id)
        
        # delete BetOptions instances not included in update
        instance.options.exclude(id__in=option_ids).delete()
        return instance


class BetParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetParticipant
        fields = ('id', 'user', 'bet', 'chosen_option', 'amount', 'created_at', 'updated_at')

class BetCreateSerializer(BetSerializer):
    options = BetOptionSerializer(many=True, required=False)

    class Meta:
        model = Bet
        fields = ('id', 'title', 'description', 'is_public', 'options')
        read_only_fields = ('creator',)

    def validate(self, attrs):
        self.validate_options(attrs.get('options', []))
        return super().validate(attrs)

    def create(self, validated_data):
        request = self.context.get('request')
        if not request.user.is_authenticated:
            raise serializers.ValidationError('You must be logged in to create a bet.')

        validated_data['creator'] = request.user

        options_data = validated_data.pop('options', [])
        bet = Bet.objects.create(**validated_data)

        for option_data in options_data:
            BetOption.objects.create(bet=bet, **option_data)

        return bet
