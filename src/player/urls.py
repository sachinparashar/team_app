from django.urls import path
from . views import PlayerDetailView

app_name = 'player'

urlpatterns = [
    path('<slug:slug>/detail/', PlayerDetailView.as_view(), name="player_detail")
]