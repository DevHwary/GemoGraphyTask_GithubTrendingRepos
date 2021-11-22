import datetime
from rest_framework import status
from rest_framework.test import APITestCase
import json


class GithubTests(APITestCase):
    """
    API View tests
    """
    def test_fetch_github_url_repos(self):
        url = '/github/trending_repos/'
        response = self.client.get(url)
        result = json.loads(response.content)   

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(result), dict )
        self.assertEqual(type(result['Python']["Number of repos"]), int )
