from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserAuthenticationTest(TestCase):
    def test_register_page(self):
        """Tests if the registration was successful"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registration")

    def test_user_registration(self):
        """Tests if the user can log in successfully"""
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'Mitch2002@',
            'password2': 'Mitch2002@'
        })
        self.assertEqual(response.status_code, 302)  # Goes to login page
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login_page(self):
        """Tests if the login page works"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_user_login(self):
        """Tests if the user can login"""
        # Makes the user
        user = User.objects.create_user(username='testuser', password='password12345')
