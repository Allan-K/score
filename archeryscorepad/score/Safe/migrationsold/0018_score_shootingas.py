# Generated by Django 3.2.9 on 2022-01-13 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0017_alter_score_archer'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='shootingas',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='score.age'),
            preserve_default=False,
        ),
    ]
