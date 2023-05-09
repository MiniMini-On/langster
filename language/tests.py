from rest_framework.test import APITestCase
from rest_framework import status


class TestLanguagePost(APITestCase):
    def setUp(self):
        self.url = '/api/language/training'
    
    def test_language_wrong_url(self):
        wrong_url = '/api/language/items'
        data = {}
        response = self.client.post(wrong_url, data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_language_empty_data(self):
        data = {}
        response = self.client.post(self.url, data)
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    def test_language_created(self):
        data = {'content':'학습시킬 데이터'}
        response = self.client.post(self.url, data)
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestLanguageGet(APITestCase):
    def setUp(self):
        self.url = '/api/language/test'
    
    def test_language_wrong_url(self):
        wrong_url = '/api/language/items'
        data = {}
        response = self.client.post(wrong_url, data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_language_empty_data(self):
        data = {}
        response = self.client.post(self.url, data)
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    def test_language_created(self):
        data = {'input':'테스트 할 문장'}
        response = self.client.post(self.url, data)
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)   
        self.assertEqual(response.data['output'], 0)   
 
      
