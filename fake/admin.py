from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Utilisateur, UserAdmin)
admin.site.register(Video)
admin.site.register(Commenter)
admin.site.register(Playlist)




