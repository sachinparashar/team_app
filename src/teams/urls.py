from django.urls import path
from . views import TeamListView ,TeamDetailView

app_name = 'teams'

urlpatterns = [
    path('', TeamListView.as_view(), name="team_list"),
    path('<slug:slug>/detail/', TeamDetailView.as_view(), name="team_detail")
] 

