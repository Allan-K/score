# Generated by Django 3.2.9 on 2021-12-21 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0003_score_rndname'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='bowtype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='score.bowtype'),
        ),
    ]
