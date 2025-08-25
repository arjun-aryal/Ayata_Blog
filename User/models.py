from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
import uuid
from .manager import CustomManager 

class CustomUser(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True, editable=False)
    name = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(max_length=50,unique=True,blank=False,null=False)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    
    objects = CustomManager()
    
    def __str__(self):
        return self.name

    