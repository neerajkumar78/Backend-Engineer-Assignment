from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    #user = models.OneToOneField(User,on_delete=models.CASCADE)
    #portfolio_site = models.URLField(blank=True)
    #Semail= models.CharField(max_length=100,widget= forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    #profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #signup_confirmation = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
