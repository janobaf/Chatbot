from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from .managers import UserManager

# Create your models here.
class usuario(AbstractBaseUser,PermissionsMixin):
    roles_choices=(
        ("A",'Admin'),
        ('U','user')
    )

    username= models.CharField(max_length=50,unique=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="imagenes")
    roles = models.CharField(max_length=1,choices=roles_choices)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD='username'
   # REQUIRED_FIELDS=[]
    
    objects=UserManager()