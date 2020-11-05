from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import VideoSerializer, CommenterSerializer, GetVideoSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from fake.models import *
import json
from controllers.modelControl import *
from moviepy.editor import VideoFileClip
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class GetAllVideoView(ListAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Video.objects.all()
    serializer_class = GetVideoSerializer


class GetAbonneCountView(APIView):

    def get(self, request):
        
        iduser = request.GET['iduser']

        user = Utilisateur.objects.get(id=iduser)

        numberAbonne = user.abonne.count()

        return Response(data={"message":numberAbonne}, status=status.HTTP_200_OK)



class VideoView(APIView):

    def post(self,request):

        form = VideoSerializer(data=request.data)
        if form.is_valid():
            url = form.validated_data.get('video')
            image = form.validated_data.get('coverImage')
            nom = form.validated_data.get('nom')
            description = form.validated_data.get('description')
            video = Video(video=url,coverImage=image,nom=nom,description=description,owner=request.user)
            video.save()
            video.refresh_from_db()
            clip = VideoFileClip(video.video.path)
            video.duree = clip.duration
            video.save()

            return Response({"message":"Ok"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":form.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request):

        idvideo = request.GET['id']

        video = Video.objects.get(id=idvideo)
        data = dict()

        data['url'] = video.video.url
        data['cover'] = video.coverImage.url
        data['vue'] = video.user_vue.count()
        data['like'] = video.user_like.count()
        #data['dislike'] = video.user_dislike.count()
        data['comment'] = video.commenter_set.count()
        data['idvideo'] = video.id 
        try:
            data['userCover'] = video.owner.profilePicture.url
        except:
            pass
        data['username'] = video.owner.username
        data['date'] = str(video.date.date())
        data['heure'] = str(video.date.time())
        data['duree'] = video.duree
        data['nomVideo'] = video.nom

        #data = json.dumps(data)

        return Response(data=data, status=status.HTTP_200_OK)





class CommentaireView(APIView):

    """
    The comment !

    id:Id video
    """

    def get(self, request):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        idvideo = request.GET['id']
        video = Video.objects.get(id=idvideo)

        serializer = CommenterSerializer(video.commenter_set.all(), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        idvideo = request.data['idvideo']
        contenue = request.data['contenue']
        video = Video.objects.get(id=idvideo)

        commentaire = Commenter.objects.create(contenue=contenue, video=video, utilisateur=request.user)

        commentaire.save()

        return Response({"message":"ok"}, status=status.HTTP_200_OK)

class LikeVideoView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request):

        idvideo = request.GET['idvideo']

        val = likeVideo(request, idvideo)

        if val:
            return Response({"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"dejas like"}, status=status.HTTP_400_BAD_REQUEST)

class LikeComment(APIView):
    pass

class DislikeVideoView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request):

        idvideo = request.GET['idvideo']

        val = dislikeVideo(request, idvideo)

        if val:
            return Response({"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"dejas dislike"}, status=status.HTTP_400_BAD_REQUEST)
    

class DislikeComment(APIView):
    pass 

class SabonneView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request):

        username = request.GET['username']
        val = sabonne(request, username)

        if val:
            return Response({"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"dejas abonne"}, status=status.HTTP_400_BAD_REQUEST)


class DesabonneView(APIView):


    permission_classes = [IsAuthenticated]


    def get(self, request):

        username = request.GET['username']
        val = desabonne(request, username)

        if val:
            return Response({"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"dejas desabonne"}, status=status.HTTP_200_OK)
    


class PlaylistView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        val = createPlaylist(request)

        return Response({"message":"ok"}, status=status.HTTP_200_OK)

  

class AddVideoPlaylistView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        idvideo = request.data['idvideo']
        idplaylist = request.data['idplaylist']

        val = addVideoOnPlaylist(request, idvideo, idplaylist)

        if val:
            return Response({"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"dejas ajouter"}, status=status.HTTP_400_BAD_REQUEST)


class DeleteVideoPlaylistView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        idvideo = request.data['idvideo']
        idplaylist = request.data['idplaylist']

        val = addVideoOnPlaylist(request, idvideo, idplaylist)

        if val:
            return Response({"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"dejas suprimer"}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = Utilisateur.objects.get(username=request.GET['username'])

        data = dict()

        data['username'] = user.username
        data['profilePicture'] = user.profilePicture.url 

        #data = json.dumps(data)

        return Response(data=data, status=status.HTTP_200_OK)