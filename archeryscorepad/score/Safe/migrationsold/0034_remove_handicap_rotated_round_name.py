# Generated by Django 3.2.9 on 2022-01-31 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0033_auto_20220131_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handicap_rotated',
            name='round_name',
        ),
    ]
