from django.contrib import admin
from . models import Teams,Match,Points
# Register your models here.
admin.site.site_header = 'Cricket App admin'
admin.site.site_title = 'Cricket App admin'
admin.site.index_title = 'Cricket App administration'

class AdminTeams(admin.ModelAdmin):
    model = Teams
    list_display = ('title', 'slug', 'club_state')
    search_fields = ['title','slug', 'club_state']

class AdminMatch(admin.ModelAdmin):
    model = Match
    list_display = ('team1','team2','winner')
    search_fields = ['team1__title']

class AdminPoints(admin.ModelAdmin):
    model: Points
    list_display = ('teams','team_points')
    search_fields = ['teams__title','team_points']

admin.site.register(Teams, AdminTeams)
admin.site.register(Match, AdminMatch)
admin.site.register(Points, AdminPoints)