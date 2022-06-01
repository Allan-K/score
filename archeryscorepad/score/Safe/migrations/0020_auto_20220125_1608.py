# Generated by Django 3.2.9 on 2022-01-25 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0019_auto_20220114_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classification', to='score.classification'),
        ),
        migrations.AlterField(
            model_name='score',
            name='rndname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round', to='score.round'),
        ),
    ]
