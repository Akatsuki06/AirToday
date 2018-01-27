from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,location,coordinates):
        if not email:
            raise ValueError('email ?')
        if not password:
            raise ValueError('password?')


        user = self.model(email= self.normalize_email(email),
                        location = location,
                         coordinates = coordinates )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password,'admin','admin')
        user.is_staff = True
        user.is_superuser=True
        user.save()
        return user

#its neccessary to have PermissionsMixin with AbstractBaseUser
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=150, unique = True, null = False, blank = False)
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=150)#contains lon and lat
    coordinates = models.CharField(max_length=20)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []#field for super user creation

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
