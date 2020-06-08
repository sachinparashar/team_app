from django.shortcuts import render,get_object_or_404
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
        HTTP_200_OK, 
        HTTP_400_BAD_REQUEST,
        HTTP_500_INTERNAL_SERVER_ERROR,
        HTTP_400_BAD_REQUEST
    )

from rest_framework.permissions import IsAuthenticated
from .serializers import TeamsListSerializer
from player.api.serializers import PlayerListSerializer
from teams.models import Teams
from player.models import Players
class TeamsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            queryset = Teams.objects.all()
            serializer = TeamsListSerializer(queryset, many=True)
            return Response({'status': True, 
                            'message': "Teams List",
                            'teams' : serializer.data
                            },
                            status=HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 
                            'message': str(e),
                            'response' : None,
                            'request': request.data},
                            status=HTTP_500_INTERNAL_SERVER_ERROR)

class TeamDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,**kwargs):
        try:
            slug = self.kwargs.get('slug')
            queryset = Teams.objects.get(slug = slug)
            print(queryset.slug)
            playerset = Players.objects.filter(team_id = queryset.teams_id)
            serializer = TeamsListSerializer(queryset)
            if playerset.count()>0:
                player_serializer = PlayerListSerializer(playerset, many=True)

            return Response({'status': True, 
                                'message': "Team Details",
                                'team_detail' : serializer.data,
                                'players': player_serializer.data
                                },
                                status=HTTP_200_OK)

        except Exception as e:
            return Response({
                'status':False,
                'message':str(e)
            },
            status = HTTP_500_INTERNAL_SERVER_ERROR
            )