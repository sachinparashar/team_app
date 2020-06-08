from django.shortcuts import render ,get_object_or_404
from django.http import Http404
from django.views.generic import ListView , DetailView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Teams
from player.models import Players

# Create your views here.

class TeamListView(LoginRequiredMixin,ListView):
    model = Teams
    context_name = 'teams_list'
    login_url = '/accounts/login/'
    # paginate_by  = 5

    def get_queryset(self):
        return Teams.objects.values('title','logo','slug').order_by('title')


class TeamDetailView(LoginRequiredMixin,MultipleObjectMixin,DetailView):
    model = Teams
    paginate_by=5

    def get_object(self, **kwargs):
        return get_object_or_404(Teams.objects.only('teams_id','slug','title','logo'),slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        team_players = Players.objects.filter(team_id = self.object.teams_id ).values('last_name','first_name','logo','slug').order_by('first_name')
        context = super(TeamDetailView, self).get_context_data(object_list=team_players,**kwargs)
        return context