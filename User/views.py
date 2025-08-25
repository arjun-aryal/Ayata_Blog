from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .token import CustomTokenObtainPairSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import CustomUser
from .serializer import UserRegistrationSerializer,UserLoginSerializer,UserProfileUpdateSerializer,UserPasswordUpdateSerializer

from rest_framework.permissions import IsAuthenticated

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserRegistrationView(APIView):
    def post(self,request):
        serializer = UserRegistrationSerializer(data = request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                token_serializer = CustomTokenObtainPairSerializer(data={
                'email': request.data.get('email'),
                'password': request.data.get('password')
            })
                if token_serializer.is_valid():
                    tokens = token_serializer.validated_data

                    return Response({
                        'refresh': str(tokens.get("refresh")),
                        'access': str(tokens.get("access"))
                     },status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data = request.data)

        if serializer.is_valid():
            
            try:
                token_serializer = CustomTokenObtainPairSerializer(data={
                'email': request.data.get('email'),
                'password': request.data.get('password')
            })
                if token_serializer.is_valid():
                    tokens = token_serializer.validated_data

                    return Response({
                        'refresh': str(tokens.get("refresh")),
                        'access': str(tokens.get("access"))
                     },status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserProfileUpdateView(APIView):
    permission_classes= [IsAuthenticated]

    def get(self,request):
        user = request.user
        serializer = UserProfileUpdateSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request):
        user = request.user
        serializer = UserProfileUpdateSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"user": serializer.data},status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserPasswordUpdateView(APIView):

    permission_classes= [IsAuthenticated]
    def put(self,request):
        serializer = UserPasswordUpdateSerializer(data=request.data, context = {"request" : request})
        
        if serializer.is_valid():
            serializer.update(request.user, serializer.validated_data) 

            return Response("Password Updated Successfully", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

