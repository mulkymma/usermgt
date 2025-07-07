from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='pass')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('pass'))
# Create your tests here.
