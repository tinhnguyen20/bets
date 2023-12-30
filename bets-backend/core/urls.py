from django.urls import path
from .views import (
    BetCreateView,
    BetListCreateView, BetRetrieveUpdateDestroyView,
    BetOptionListCreateView, BetOptionRetrieveUpdateDestroyView,
    BetParticipantListCreateView, BetParticipantRetrieveUpdateDestroyView
)

urlpatterns = [
    path('bets/', BetListCreateView.as_view(), name='bet-list-create'),
    path('bets/create/', BetCreateView.as_view(), name='bet-create'),
    path('bets/<int:pk>/', BetRetrieveUpdateDestroyView.as_view(), name='bet-detail'),

    # path('bet-options/', BetOptionListCreateView.as_view(), name='bet-option-list-create'),
    # path('bet-options/<int:pk>/', BetOptionRetrieveUpdateDestroyView.as_view(), name='bet-option-detail'),

    path('participants/', BetParticipantListCreateView.as_view(), name='participant-list-create'),
    path('participants/<int:pk>/', BetParticipantRetrieveUpdateDestroyView.as_view(), name='participant-detail'),
]
