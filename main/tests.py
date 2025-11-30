from django.test import TestCase, Client
from django.urls import reverse


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        """Test that index page loads successfully"""
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)

    def test_api_hello(self):
        """Test hello API endpoint"""
        response = self.client.get(reverse('main:api_hello'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('message', data)

    def test_api_status(self):
        """Test status API endpoint"""
        response = self.client.get(reverse('main:api_status'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'running')
        self.assertIn('app', data)
