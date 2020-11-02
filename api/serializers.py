from rest_framework.serializers import ModelSerializer
from  rest_framework import serializers
from fake.models import *

class VideoSerializer(ModelSerializer):

    class Meta:
        model = Video
        fields = ['video', 'coverImage', 'nom', 'description']
        

class GetVideoSerializer(ModelSerializer):


    class Meta:
        model = Video
        fields = ('__all__')
        depth = 1


class CommenterSerializer(ModelSerializer):

    class Meta:
        model = Commenter 
        fields = ('__all__')
        depth = 1


class UserSerializer(ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = ('__all__')