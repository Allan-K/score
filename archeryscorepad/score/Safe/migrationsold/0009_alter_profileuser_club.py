# Generated by Django 3.2.9 on 2022-01-06 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0008_auto_20220106_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='score.club'),
        ),
    ]
