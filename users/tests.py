from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUsersNewUser(TestCase):

    def test_user_instance(self):
        db = get_user_model()
        user = db.objects.create_superuser('test@user.com', 'username', 'nickname', 'password')

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

        self.assertEqual(str(user), 'username')

        with self.assertRaises(ValueError):
            db.objects.create_superuser('', 'username', 'nickname', 'password')

        with self.assertRaises(ValueError):
            db.objects.create_superuser('test@user.com', 'username', 'nickname', 'password', is_staff=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser('test@user.com', 'username', 'nickname', 'password', is_superuser=False)

