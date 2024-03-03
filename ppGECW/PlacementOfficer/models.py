from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class ProfilePO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(blank=False,max_length=30,null=False,default="WYD")
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True,default=settings.DEFAULT_PROFILE_PIC)