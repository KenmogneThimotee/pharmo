from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Utilisateur(AbstractUser):
    sexe = models.CharField(max_length=1)
    profilePicture = models.ImageField(upload_to='imagesProfile', null=True)
    baniere = models.ImageField(upload_to='imagesBanniere', null=True)
    abonne = models.ManyToManyField('self')
    vue = models.ManyToManyField('Video', related_name='user_vue')
    like = models.ManyToManyField('Video', related_name='user_like')
    dislike = models.ManyToManyField('Video', related_name='user_dislike')
    voir = models.ManyToManyField('Video', related_name='user_voir')
    reponse = models.ManyToManyField('Commenter', related_name='user_reponse')
    commenter = models.ManyToManyField('Video', through='Commenter')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'password','profilePicture','baniere','sexe']


class Video(models.Model):
    video = models.FileField(upload_to='videosFile')
    nom = models.CharField(max_length=50)
    description = models.TextField()  
    duree = models.BigIntegerField(null=True)
    date = models.DateTimeField(auto_now=True)
    coverImage = models.ImageField(upload_to='coverImages')
    owner = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    

class Commenter(models.Model):
    contenue = models.TextField()
    date = models.DateTimeField(auto_now=True)
    utilisateur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE, related_name='commentateur')
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    like = models.ManyToManyField('Utilisateur', related_name='comment_like')
    dislike = models.ManyToManyField('Utilisateur', related_name='comment_dislike')

    class Meta:

        ordering = ['-date']

    

class Playlist(models.Model):
    nom = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    video = models.ManyToManyField('Video')
    utilisateur = models.ForeignKey('Utilisateur',on_delete=models.CASCADE, related_name='owner')