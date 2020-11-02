from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django import forms


class UtilisateurCreationForm(UserCreationForm):
    CHOICES = [('M', 'Masculin'), ('F', 'Feminin')]

    sexe = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


    class Meta:
        model = Utilisateur
        fields = ['first_name','last_name','sexe','profilePicture','baniere','username']



class UploadForm(forms.ModelForm):


    class Meta:
        model = Video
        fields = ['video', 'nom', 'description','coverImage']