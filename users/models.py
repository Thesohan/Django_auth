from django.db import models,transaction
from django.utils import timezone
from django.contrib.auth.models import (
     AbstractBaseUser,PermissionsMixin
)
from django.contrib.auth.models import (
     AbstractBaseUser,PermissionsMixin,BaseUserManager
)
# Create your models here.
class UserManager(BaseUserManager):
     
     def _create_user(self,email,password,**kwargs):
          """
          Creates and saves a User with the given email,and password.
          """
          
          if not email:
               raise ValueError('Email required.')
          try:
               with transaction.atomic():
                    user = self.model(email=email,**kwargs)
                    user.set_password(password)
                    user.save(using = self._db)
                    return user
          except:
               raise
          
     def create_user(self, email, password=None, **kwargs):
          
          kwargs.setdefault('is_staff', False)
          kwargs.setdefault('is_superuser', False)
          return self._create_user(email, password, **kwargs)
     
     def create_superuser(self, email, password, **kwargs):
          kwargs.setdefault('is_staff', True)
          kwargs.setdefault('is_superuser', True)
          return self._create_user(email, password=password, **kwargs)

class User(AbstractBaseUser,PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
 
    """
    email = models.EmailField(max_length=40,unique=True)
    first_name = models.CharField(max_length=39,blank=True)
    last_name = models.CharField(max_length=40,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    joined_date = models.DateTimeField(default=timezone.now)
    
    objects = UserManager() 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return self