from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=50, auto_created=False, )
    last_name = models.CharField(max_length=50, auto_created=False)
    age = models.IntegerField(default=0, )
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
