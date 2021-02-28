from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DrProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional fields
    specialisation = models.CharField(max_length=100,blank=False)
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return "Dr. "+self.user.first_name+" "+self.user.last_name
