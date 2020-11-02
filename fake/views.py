from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from moviepy.editor import VideoFileClip
from django.conf import settings
from django.http import JsonResponse
import json

# Create your views here.


def home(request):
    
    videos = Video.objects.all()
    user = request.user
    return render(request, 'index.html', {"videos":videos, "user":user} )

def OneVideo(request, id):
    video = Video.objects.get(id=id)
    url = video.video
    url = json.dumps({"url":url})
    return JsonResponse(url)

def video(request,id):  
    video = Video.objects.get(id=id)
    videos = Video.objects.all()
    user = request.user

    return render(request, 'single_video_page.html',{"video":video,"similar_videos":videos,"user":user})

@login_required(login_url='/login')
def playlist(request, id):

    videos = Playlist.objects.get(id=id).video.all()

    return render(request, 'single_video_playlist.html', {"videos": videos})

@login_required(login_url='/login')
def channel(request, id):

    channels = [ user for user in Utilisateur.objects.all() if user.is_superuser != True and user.id != id]
    print(channels)
    user = Utilisateur.objects.get(id=id)
    return render(request, 'Single_Channel_Channels.html', {"user": user, "channels":channels})

@login_required(login_url='/login')
def history(request):

    video_list = request.user.vue.all()
    return render(request, 'History_Page.html',{"video_list":video_list})

@login_required(login_url='/login')
def BrowseChannel(request):

    user_list = [ user for user in Utilisateur.objects.all() 
    if user.is_superuser != True and user.id != request.user.id]
    return render(request, 'Browse_Channels.html', {"user_list": user_list})

@login_required(login_url='/login')
def subscription(request):

    user_list = request.user.abonne.all()
    return render(request, 'subscriptions.html', {"user_list": user_list})

def signup(request):

    if request.POST:
        form = UtilisateurCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.profilePicture = request.FILES['profilePicture']
            user.baniere = request.FILES['baniere']
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                return redirect('/login')
            else:
                return render(request, 'signup.html', {"form": form})
        else:
            return render(request, 'signup.html', {"form": form})
    else:
        form = UtilisateurCreationForm()
        return render(request, 'signup.html', {"form": form})

@login_required(login_url='/login')
def logoutView(request):
    logout(request)
    return redirect('/loginView')

@login_required(login_url='/login')
def signoutView(request):
    logout(request)

    return redirect("/login")


@login_required(login_url='/login')
def upload(request):

    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            url = form.cleaned_data.get('video')
            image = form.cleaned_data.get('coverImage')
            nom = form.cleaned_data.get('nom')
            description = form.cleaned_data.get('description')
            video = Video(video=url,coverImage=image,nom=nom,description=description,owner=request.user)
            video.save()
            video.refresh_from_db()
            clip = VideoFileClip(video.video.path)
            video.duree = clip.duration
            video.save()

            return redirect('/upload')
        else:
            print(form.errors)
            return render(request,'Upload_Video.html',{"form": form})
    else:
        print("test upload")
        return render(request,'Upload_Video.html')

def searchVideo(request, mots):

    video = Video.objects.filter(nom__in=mots)

    return render(request, 'search_views', {"videos":video})

def likeVideoView(request):

    videos = request.user.like.all()

    return render(request, 'like.html.html',{"videos":videos})

