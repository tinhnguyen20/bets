from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Bet, BetOption, BetParticipant

class BetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.url = '/bets/create/'
        self.url_update = '/bets/{}/'
    
    def tearDown(self):
        Bet.objects.all().delete()
        BetOption.objects.all().delete()
        BetParticipant.objects.all().delete()

    def test_create_bet_with_options(self):
        """
        A bet with two options
        """
        data = {
            "title": "49ers beat the Ravens",
            "description": "A bet about football",
            # "creator": self.user.id,
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
            # "creator": self.user.id,
            "is_public": True,
            "options": []
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Bet.objects.count(), 0)
        self.assertEqual(BetOption.objects.count(), 0)

    def test_create_bet_multiple_options(self):
        """
        A bet with multiple options
        """
        data = {
            "title": "Who becomes the F1 2024 Champion",
            "description": "NYE 2069",
            # "creator": self.user.id,
            "is_public": True,
            "options": [
                {"title": "Max Verstappen"},
                {"title": "Lewis Hamilton"},
                {"title": "Logan Sargeant"},
            ]
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bet.objects.count(), 1)
        self.assertEqual(BetOption.objects.count(), 3)
    
    def test_create_invalid_bet_multiple_options(self):
        """
        A bet with multiple options
        """
        data = {
            "title": "Who falls asleep first tonight?",
            "description": "",
            # "creator": self.user.id,
            "is_public": True,
            "options": [
                {"title": "Bob"},
                {"title": "Joe"},
                {"title": "Joe"},
            ]
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_update_bet_multiple_options(self):
        """
        Updating a bet with a new option
        """
        data = {
            "title": "Who becomes the F1 2024 Champion",
            "description": "NYE 2069",
            # "creator": self.user.id,
            "is_public": True,
            "options": [
                {"title": "Max Verstappen"},
                {"title": "Lewis Hamilton"},
                {"title": "Logan Sargeant"},
            ]
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bet.objects.count(), 1)
        self.assertEqual(BetOption.objects.count(), 3)

        bet_id = response.data['id']

        data['options'].append({
            'title': 'Oscar Piastri'
        })

        updated_data = response.data
        updated_data['options'].append({
            'title': 'Oscar Piastri'
        })
        updated_response = self.client.put(self.url_update.format(bet_id), updated_data, format='json')
        self.assertEqual(updated_response.status_code, status.HTTP_200_OK)
        self.assertEqual(Bet.objects.count(), 1)
        self.assertEqual(BetOption.objects.count(), 4)

    def test_create_update_bet_multiple_duplicate_options(self):
        """
        An invalid bet with multiple duplicate options
        """
        data = {
            "title": "Who becomes the F1 2024 Champion",
            "description": "NYE 2069",
            # "creator": self.user.id,
            "is_public": True,
            "options": [
                {"title": "Max Verstappen"},
                {"title": "Lewis Hamilton"},
                {"title": "Logan Sargeant"},
            ]
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bet.objects.count(), 1)
        self.assertEqual(BetOption.objects.count(), 3)

        bet_id = response.data['id']

        updated_data = response.data
        updated_data['options'].append({
            'title': 'Logan Sargeant'
        })
        updated_response = self.client.put(self.url_update.format(bet_id), updated_data, format='json')
        self.assertEqual(updated_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_update_bet_invalid_options(self):
        """
        Invaid update, leaving less than 2 bet options
        """
        data = {
            "title": "Who becomes the F1 2024 Champion",
            "description": "NYE 2069",
            # "creator": self.user.id,
            "is_public": True,
            "options": [
                {"title": "Max Verstappen"},
                {"title": "Lewis Hamilton"},
                {"title": "Logan Sargeant"},
            ]
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bet.objects.count(), 1)
        self.assertEqual(BetOption.objects.count(), 3)

        bet_id = response.data['id']

        updated_data = response.data
        updated_data['options'] = []
        updated_response = self.client.put(self.url_update.format(bet_id), updated_data, format='json')
        self.assertEqual(updated_response.status_code, status.HTTP_400_BAD_REQUEST)
