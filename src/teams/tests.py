from django.test import TestCase, Client
from django.urls import reverse,resolve 
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from teams.models import Teams
from teams.views import TeamListView, TeamDetailView

User = get_user_model()
class TestTeamModel(TestCase):
    def setUp(self):
        obj1 = Teams.objects.create(title = "CSK", slug = "csk", club_state = "Chennai")
        obj2 = Teams.objects.create(title = "DD", slug = "dd", club_state = "Delhi")

    def test_team_model(self):
        obj1 = Teams.objects.get(slug='csk')
        obj2 = Teams.objects.get(slug = "dd")
        self.assertEquals(obj1.title, 'CSK')
        self.assertEquals(obj2.title, 'DD')

class BaseClass(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test1',
            email='abc1@gmail.com',
            first_name='t',
            last_name='u',
            password='password'
        )
        
        self.team = Teams.objects.create(
            title="My Team",
            slug="my-team",
            club_state="Mumbai"
        )

class TestTeamsView(BaseClass):    
    def test_team_list_view_with_valid_user(self):
        request = self.factory.get('/team/')
        request.user = self.user
        response = TeamListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'teams/teams_list.html')
    
    def test_team_list_view_with_anonymous_user(self):
        request = self.factory.get('/team/')
        request.user = AnonymousUser()
        response = TeamListView.as_view()(request)
        self.assertEqual(response.status_code,302)

class TestTeamsDetailView(BaseClass):      

    def test_team_detail_view_with_valid_user(self):
        request = self.factory.get("/teams/my-team/detail")
        request.user = self.user
        response = TeamDetailView.as_view()(request, slug='my-team')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.template_name[0], 'teams/teams_detail.html')

    def test_team_detail_view_with_invalid_user(self):
        request = self.factory.get("/teams/my-team/detail")
        request.user = AnonymousUser()
        response = TeamDetailView.as_view()(request, slug='my-team')
        self.assertEqual(response.status_code,302)