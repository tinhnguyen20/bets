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

class BetListCreateView(generics.ListCreateAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer

    @authentication_classes([])
    def list(self, request, *args, **kwargs):
        print(request.user)
        print(request.session.get("user"))
        if request.user.is_authenticated:
            print('Authenticated')
        else:
            print('NOT Authenticated')

        return super().list(request, *args, **kwargs)

class BetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        queryset = BetOption.objects.filter(bet=instance).prefetch_related('participants')
        bet_options_serializer = BetOptionSerializer(queryset, many=True)

        data = {
            'bet': self.get_serializer(instance),
            'bet_options': bet_options_serializer.data,
        }

        return Response(data)

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
