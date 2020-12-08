from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Content(models.Model):
    url=models.TextField() 
    response=models.TextField() 
    username=models.ManyToManyField(User)

    def __unicode__(self):
        return "{0} {1} {2}".format(
            self.pk, self.url, self.response)
