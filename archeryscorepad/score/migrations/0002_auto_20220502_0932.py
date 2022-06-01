# Generated by Django 3.2.9 on 2022-05-02 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='eleven',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='roundscore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot_1', models.IntegerField(blank=True, default=0, null=True)),
                ('shot_2', models.IntegerField(blank=True, default=0, null=True)),
                ('shot_3', models.IntegerField(blank=True, default=0, null=True)),
                ('shot_4', models.IntegerField(blank=True, default=0, null=True)),
                ('shot_5', models.IntegerField(blank=True, default=0, null=True)),
                ('shot_6', models.IntegerField(blank=True, default=0, null=True)),
                ('end_1', models.IntegerField(blank=True, default=0, null=True)),
                ('archer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score.round')),
            ],
        ),
    ]
