from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user_identify = models.ForeignKey(User,on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    website = models.URLField(default="")
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user_identify.username


class article(models.Model):
    author = models.CharField(max_length=20)
    image = models.FileField()
    title = models.CharField(max_length=150)
    details = models.TextField()

    def __str__(self):
        return self.author








def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user_identify=kwargs['instance'])


post_save.connect(create_profile,sender=User)


