from . import serializers
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework import status


class FeedbackView(APIView) :

    def post(self, request):
       
        serializer = serializers.FeedbackSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
