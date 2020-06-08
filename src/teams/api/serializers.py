from rest_framework.serializers import ModelSerializer
from teams.models import Teams

class TeamsListSerializer(ModelSerializer):
    class Meta:
        model = Teams
        fields="__all__"