from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length = 128)
    class Meta:
        model = CustomUser
        fields = ["name","email","password","confirm_password"]
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
        }

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        if password!=confirm_password:
            raise serializers.ValidationError("Password doesnot confirm")

        
        return attrs
    

    def create(self, validated_data):
        password = validated_data.pop("password")
        _ = validated_data.pop("confirm_password")
        
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 50)
    password = serializers.CharField(max_length = 128, required=True)
    


    
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ["id","name","email"]
        read_only_fields = ["id"]
    
    def validate_email(self,value):
        user = self.instance
        if CustomUser.objects.filter(email=value).exclude(id = user.id).exists():
            return serializers.ValidationError("The Email is already in user")
        return value


class UserPasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True,max_length = 128)
    new_password = serializers.CharField(write_only=True, required=True,max_length = 128)
    confirm_password = serializers.CharField(write_only=True, required=True,max_length = 128)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect")
        return value
    
    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password Doesnot Match")
        
        return attrs
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance