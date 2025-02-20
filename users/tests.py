from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import User


class UserViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='TestPassword123'
        )

    def test_registration_view(self):
        """Тест реєстрації нового користувача"""
        response = self.client.post(reverse('users:registration'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'NewPassword123',
            'password2': 'NewPassword123',
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після реєстрації
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        """Тест логіну користувача"""
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'TestPassword123',
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після входу

    def test_profile_view(self):
        """Тест перегляду сторінки профілю"""
        self.client.login(username='testuser', password='TestPassword123')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_profile_update(self):
        """Тест оновлення профілю"""
        self.client.login(username='testuser', password='TestPassword123')
        response = self.client.post(reverse('users:profile'), {
            'first_name': 'UpdatedName',
            'last_name': 'UpdatedLastName',
            'username': 'testuser',
            'email': 'updated@example.com',
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після оновлення
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedName')
        self.assertEqual(self.user.email, 'updated@example.com')

    def test_logout_view(self):
        """Тест виходу користувача"""
        self.client.login(username='testuser', password='TestPassword123')
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)  # Перенаправлення після виходу
