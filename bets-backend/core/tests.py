from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Bet, BetOption, BetParticipant

class BetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = '/bets/create/'

    def test_create_bet_with_options(self):
        """
        A bet with two options
        """
        data = {
            "title": "49ers beat the Ravens",
            "description": "A bet about football",
            "creator": self.user.id,
            "is_public": True,
            "options": [
                {"title": "49ers GANG GANG"},
                {"title": "Ravens"}
            ]
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bet.objects.count(), 1)
        self.assertEqual(BetOption.objects.count(), 2)

    def test_create_bet_without_options(self):
        data = {
            "title": "Test Bet",
            "description": "Description of the test bet",
            "creator": self.user.id,
            "is_public": True,
            "options": []
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Bet.objects.count(), 0)
        self.assertEqual(BetOption.objects.count(), 0)
