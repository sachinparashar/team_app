from django.db import models
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

class Teams(models.Model):
    teams_id     = models.AutoField(primary_key=True)
    title        = models.CharField(max_length=200)
    slug         = models.SlugField(unique=True)
    logo         = models.ImageField(upload_to='teams_logo/',null=True, blank=True)
    club_state   = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.title and self.slug:
            self.slug = slugify(self.title)
        super(Teams, self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.title



class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    team1    = models.ForeignKey(Teams, related_name="MatchTeamOne" , on_delete=models.PROTECT)
    team2    = models.ForeignKey(Teams, related_name="MatchTeamTwo" , on_delete=models.PROTECT)
    winner   = models.ForeignKey(Teams, related_name="Winner" , on_delete=models.PROTECT)
    # created_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Matches"



class Points(models.Model):
    points_id   = models.AutoField(primary_key=True)
    teams       = models.ForeignKey(Teams, related_name = "Teams" , on_delete=models.PROTECT)
    team_points = models.DecimalField(blank=True, max_digits=10, decimal_places=2, help_text="Points")

    class Meta:
        verbose_name_plural = "Points" 

    def __str__(self):
        return self.teams.title
