from rest_framework.test import APITestCase
from rest_framework import status


class TestFeedback(APITestCase):
    def setUp(self):
        self.url = '/api/feedback/item'
    
    def test_feedback_wrong_url(self):
        wrong_url = '/api/feedback/items'
        data = {}
        response = self.client.post(wrong_url, data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_feedback_empty_data(self):
        data = {}
        response = self.client.post(self.url, data)
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_feedback_wrong_title(self):
        data = {'title':'오류', 'content':'오류발견'}
        response = self.client.post(self.url, data)
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_feedback_created(self):
        data = {'title':'E', 'content':'오류발견'}
        response = self.client.post(self.url, data)
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
 
      