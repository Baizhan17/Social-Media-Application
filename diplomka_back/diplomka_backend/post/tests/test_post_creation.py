from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from account.models import User
from post.models import Post

class AddPostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            name='testuser', 
            password='testpassword',
            email='testuser@example.com'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.url = reverse('post_create')  # Adjust this based on your URL configuration
        self.payload = {
            'body': 'Test body text',
            # Add any other required fields here
        }

    def test_add_post(self):
        initial_post_count = Post.objects.count()
        response = self.client.post(self.url, self.payload, format='json')

        # Debugging information
        print(response.status_code)
        print(response.content)  # Print response content to debug

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify if you expect a certain field in the response
        # Example:
        # self.assertIn('id', response.data)

        # Optionally, assert against the database state if needed
        self.assertEqual(Post.objects.count(), initial_post_count + 1)

    def tearDown(self):
        # Clean up any test data as needed
        pass
