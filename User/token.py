from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token =  super().get_token(user)
        token["id"] = str(user.id)
        token["name"] = user.name
        token["email"] = user.email

        if user.is_superuser  or user.is_staff:
            token["admin"] = True 
        
        return token
