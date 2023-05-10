from rest_framework import serializers
from .models import Suggestion, TestNum

class SuggestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Suggestion
        fields = '__all__'  
        
class TestNumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TestNum
        fields = '__all__'  
        

