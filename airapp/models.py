from django.db import models

# Create your models here.
from django.contrib.auth.models import User, UserManager

class UserRegistration(User):

    location = models.CharField(max_length=50)#contains long and lats
    objects = UserManager()
