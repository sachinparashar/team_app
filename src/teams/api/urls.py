from django.urls import path
from django.conf.urls import url
from . views import TeamsList ,TeamDetails

app_name = 'teams'

urlpatterns = [
    path('teams/list/', TeamsList.as_view(), name="team_list_api"),
    path('details/<slug:slug>/', TeamDetails.as_view(), name="team_detail_api")
] 