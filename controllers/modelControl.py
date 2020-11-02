from fake.models import *

def sabonne(request,id):
    user = request.user
    utilisateur = Utilisateur.objects.get(username=id)

    listAbonnement = utilisateur.abonne.all()

    if user not in listAbonnement:
        utilisateur.abonne.add(user)
        utilisateur.save()
        return True
    else:
        return False

def desabonne(request,id):
    user = request.user
    utilisateur = Utilisateur.objects.get(username=id)

    listAbonnement = utilisateur.abonne.all()

    if user in listAbonnement:
        utilisateur.abonne.remove(user)
        utilisateur.save()
        return True
    else:
        return False

def addVideoOnPlaylist(request, idvideo, idplaylist):
    playlist = Playlist.objects.get(id=idplaylist)
    video = Video.objects.get(id=idvideo)

    listvideo = playlist.video.all()

    if video not in listvideo:
        playlist.video.add(video)
        playlist.save()
        return True
    else:
        return False
    
def deleteVideoOnPlaylist(request, idvideo, idplaylist):
    playlist = Playlist.objects.get(id=idplaylist)
    video = Video.objects.get(id=idvideo)

    listvideo = playlist.video.all()

    if video in listvideo:
        playlist.video.remove(video)
        playlist.save()
        return True
    else:
        return False

def createPlaylist(request):
    user = request.user 

    nom = request.data['nom']

    playlist = Playlist(nom=nom,utilisateur=user)
    playlist.save()

    return True

def deletePlayList(request, id):

    Playlist.objects.get(id=id).delete()

    return True

def likeVideo(request, id):
    
    user = request.user 
    video = Video.objects.get(id=id)

    listvideo = user.like.all()

    if video not in listvideo:

        if video in user.dislike.all():
            user.dislike.remove(video)

        user.like.add(video)

        user.save()

        return True

    else:
        return False
    

def dislikeVideo(request, id):

    user = request.user 
    video = Video.objects.get(id=id)

    listvideo = user.dislike.all()

    if video not in listvideo:

        if video in user.like.all():
            user.dislike.remove(video)

        user.dislike.add(video)

        user.save()

        return True

    else:
        return False


def likeStatus(request, id):

    user = request.user 
    video = Video.objects.get(id=id) 

    if video in user.like.all():
        return True
    elif video in user.dislike.all():
        return False 
    else:
        return None


def getAllComment(request, idvideo):
    video = Video.objects.get(id=idvideo)

    return video.commenter_set.all()


def postComment(request, idvideo):

    video = Video.objects.get(id=idvideo)

    contenue = request.POST['contenue']

    comment = Commenter(contenue=contenue, utilisateur=request.user, video=video)

    comment.save()

    return True 



