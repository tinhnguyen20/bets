from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Bet, BetOption, BetParticipant
from .serializers import (
    BetSerializer, BetOptionSerializer,
    BetParticipantSerializer, BetCreateSerializer
)

class BetCreateView(generics.CreateAPIView):
    serializer_class = BetCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BetListView(generics.ListAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer

    def get_queryset(self):
        # Check if user is authenticated
        if self.request.user.is_authenticated:
            return Bet.objects.filter(Q(creator=self.request.user)).distinct()
            # return Bet.objects.filter(Q(participants=self.request.user) | Q(creator=self.request.user)).distinct()  # to group created/participated into one
        else:
            return Bet.objects.filter(is_public=True)

    def list(self, request, *args, **kwargs):
        print(request.user)
        query_set = self.get_queryset()
        participating_bets = Bet.objects.filter(Q(participants=self.request.user)).distinct()
        return Response({
            'participating_bets': self.serializer_class(participating_bets, many=True).data,
            'n_pbets': len(participating_bets),
            'created_bets': self.serializer_class(query_set, many=True).data,
            'n_created': len(query_set),
        })

class BetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()

    #     queryset = BetOption.objects.filter(bet=instance).prefetch_related('participants')
    #     bet_options_serializer = BetOptionSerializer(queryset, many=True)

    #     data = {
    #         'bet': self.get_serializer(instance),
    #         'bet_options': bet_options_serializer.data,
    #     }

    #     return Response(data)

class BetOptionListCreateView(generics.ListCreateAPIView):
    queryset = BetOption.objects.all()
    serializer_class = BetOptionSerializer

class BetOptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BetOption.objects.all()
    serializer_class = BetOptionSerializer

class BetParticipantListCreateView(generics.ListCreateAPIView):
    queryset = BetParticipant.objects.all()
    serializer_class = BetParticipantSerializer

class BetParticipantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BetParticipant.objects.all()
    serializer_class = BetParticipantSerializer
