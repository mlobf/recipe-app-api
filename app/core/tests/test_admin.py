from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    #Creating a setup function, that is a function that runs
    #before the every test than we run.


    def setUp(self):
        #Will consist test client creating a new user to test
        # 
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@londonappdev.com',
            password = 'password123'
        )
        self.client.force_login(self.admin_user)