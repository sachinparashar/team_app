# Generated by Django 3.0.6 on 2020-05-29 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20200530_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='MatchTeamOne', to='teams.Teams'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='MatchTeamTwo', to='teams.Teams'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Winner', to='teams.Teams'),
        ),
    ]
