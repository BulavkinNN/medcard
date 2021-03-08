from django.test import TestCase
from medcard.models import UserAccount
from medcard.views import doctor


class UserAccountTestClass(TestCase):
    def setUp(self):
        # Установки запускаются перед каждым тестом
        pass

    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)
