from rest_framework.serializers import ModelSerializer
from player.models import Players

class PlayerListSerializer(ModelSerializer):
    class Meta:
        model = Players
        fields="__all__"