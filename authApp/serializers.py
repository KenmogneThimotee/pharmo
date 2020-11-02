from djoser.serializers import UserCreateSerializer
from fake.models import Utilisateur


class UtilisateurCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = Utilisateur
        fields = ('__all__')