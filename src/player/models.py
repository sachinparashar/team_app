from django.db import models
from teams.models import Teams

DEFAULT_TEAM_ID = 1

class Players(models.Model):
    player_id     = models.AutoField(primary_key=True)
    team_id       = models.ForeignKey(Teams, verbose_name='Team' , default=DEFAULT_TEAM_ID, on_delete=models.CASCADE)
    first_name    = models.CharField(verbose_name = 'firstName', max_length=200,null=False, blank=False)
    last_name     = models.CharField(verbose_name = 'lastName', max_length=200,null=False, blank=False)
    slug          = models.SlugField(unique=True)
    logo          = models.ImageField(upload_to='teams_logo/',null=True, blank=True)
    jersey_number = models.IntegerField()
    country       = models.CharField(verbose_name = 'country', max_length=100, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.last_name and not self.first_name and self.slug:
            self.slug = slugify(self.last_name+'-'+self.first_name)
        super(Players, self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = "Players"

    def __str__(self):
        return self.first_name


class PlayerHistory(models.Model):
    player_history_id = models.AutoField(primary_key=True)
    player_id         = models.ForeignKey(Players, on_delete=models.CASCADE)
    matches           = models.IntegerField()
    run               = models.IntegerField()
    highest_score     = models.IntegerField()
    fifties           = models.IntegerField()
    hundred           = models.IntegerField()

    class Meta:
        verbose_name_plural = "Player History"

    def __str__(self):
        return self.player_id.first_name