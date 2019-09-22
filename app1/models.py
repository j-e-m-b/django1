from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    '''
    Perfil de usuario
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # portafolio
    portfolio = models.URLField(blank=True)
    # imagen de perfil
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Topic(models.Model):
    '''
    Modelo
    '''
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    '''
    Modelo
    '''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    '''
    Modelo
    '''
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

        