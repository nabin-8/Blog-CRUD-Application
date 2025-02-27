from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status


def RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            
            if not serializer.is_valid():
                return Response({
                    
                    'data': serializer.errors,
                    "message": "something went wrong"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({
                
                'data': serializer.data,
                "message": "user created successfully"
            }, status=status.HTTP_201_CREATED)
                
        except Exception as e:
                return Response({
                    
                    'data': {},
                    "message": "something went wrong"
                }, status=status.HTTP_400_BAD_REQUEST)