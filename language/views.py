from . import serializers
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework import status
from tensorflow import keras
import tensorflow as tf
from konlpy.tag import Okt
import pickle
import re
from .models import TestNum 
from django.db import transaction


class SuggestionView(APIView) :

    def post(self, request):
       
        serializer = serializers.SuggestionSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
class TestNumView(APIView) :

    def get(self, request):
        try:
            number = TestNum.objects.last()
            if number == None:
                TestNum.objects.create(number = 1)
                number = TestNum.objects.last()
            serializer = serializers.TestNumSerializer(number)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
            
        except TestNum.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
class LanguageTestView(APIView) :
    @transaction.atomic
    def post(self, request):
        
        if not 'input' in request.data:
            return Response(data={'error':'input is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        with open('data_dict.pkl', 'rb') as f:
            mydict = pickle.load(f)
        okt = Okt()
        hangle = re.compile('[^ ㄱ-ㅣ가-힣]+')
        model = tf.keras.models.load_model('language.h5')
        
        X = request.data['input']
        X = hangle.sub('', X)
        X = [okt.morphs(X, stem = True, norm = True)]
        tokenizer = keras.preprocessing.text.Tokenizer(filters='')
        tokenizer.word_index = mydict
        X = tokenizer.texts_to_sequences(X)
        X = keras.preprocessing.sequence.pad_sequences(X, value=0, padding='post', maxlen=255)

        number = TestNum.objects.last()
        number.number += 1
        number.save()
        
        res = model.predict(X)
    
        if res >= 0.5:
            return Response(data={'output': 1}, status=status.HTTP_200_OK)
        elif res < 0.5:
            return Response(data={'output': 0}, status=status.HTTP_200_OK)