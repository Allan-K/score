# Generated by Django 3.2.9 on 2021-12-18 15:05

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ageband', models.CharField(max_length=14)),
                ('maxage', models.IntegerField(verbose_name='Age Range')),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='BowType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bowtype', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Handicap',
            fields=[
                ('handicap', models.IntegerField(primary_key=True, serialize=False)),
                ('WA1440_Gents', models.IntegerField(blank=True, default='', null=True)),
                ('WA1440_Ladies', models.IntegerField(blank=True, default='', null=True)),
                ('Half_WA1440_Gents', models.IntegerField(blank=True, default='', null=True)),
                ('Half_WA1440_Ladies', models.IntegerField(blank=True, default='', null=True)),
                ('Metric_I', models.IntegerField(blank=True, default='', null=True)),
                ('Metric_II', models.IntegerField(blank=True, default='', null=True)),
                ('Metric_III', models.IntegerField(blank=True, default='', null=True)),
                ('Metric_IV', models.IntegerField(blank=True, default='', null=True)),
                ('Metric_V', models.IntegerField(blank=True, default='', null=True)),
                ('Long_Metric_Gents', models.IntegerField(blank=True, default='', null=True)),
                ('Long_Metric_Ladies', models.IntegerField(blank=True, default='', null=True)),
                ('Long_Metric_II', models.IntegerField(blank=True, default='', null=True)),
                ('Long_Metric_III', models.IntegerField(blank=True, default='', null=True)),
                ('Long_Metric_IV', models.IntegerField(blank=True, default='', null=True)),
                ('Long_Metric_V', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Metric', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Metric_II', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Metric_III', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Metric_IV', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Metric_V', models.IntegerField(blank=True, default='', null=True)),
                ('WA_900', models.IntegerField(blank=True, default='', null=True)),
                ('WA_70M', models.IntegerField(blank=True, default='', null=True)),
                ('WA_60M', models.IntegerField(blank=True, default='', null=True)),
                ('WA_50M', models.IntegerField(blank=True, default='', null=True)),
                ('WA_Standard_Bow', models.IntegerField(blank=True, default='', null=True)),
                ('Olympic_Match', models.IntegerField(blank=True, default='', null=True)),
                ('York', models.IntegerField(blank=True, default='', null=True)),
                ('Hereford', models.IntegerField(blank=True, default='', null=True)),
                ('Bristol_II', models.IntegerField(blank=True, default='', null=True)),
                ('Bristol_III', models.IntegerField(blank=True, default='', null=True)),
                ('Bristol_IV', models.IntegerField(blank=True, default='', null=True)),
                ('Bristol_V', models.IntegerField(blank=True, default='', null=True)),
                ('St_George', models.IntegerField(blank=True, default='', null=True)),
                ('Albion', models.IntegerField(blank=True, default='', null=True)),
                ('Windsor', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Windsor', models.IntegerField(blank=True, default='', null=True)),
                ('Junior_Windsor', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Junior_Windsor', models.IntegerField(blank=True, default='', null=True)),
                ('New_Western', models.IntegerField(blank=True, default='', null=True)),
                ('Long_Western', models.IntegerField(blank=True, default='', null=True)),
                ('Western', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Western', models.IntegerField(blank=True, default='', null=True)),
                ('Junior_Western', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Junior_Western', models.IntegerField(blank=True, default='', null=True)),
                ('American', models.IntegerField(blank=True, default='', null=True)),
                ('St_Nicholas', models.IntegerField(blank=True, default='', null=True)),
                ('New_National', models.IntegerField(blank=True, default='', null=True)),
                ('Long_National', models.IntegerField(blank=True, default='', null=True)),
                ('National', models.IntegerField(blank=True, default='', null=True)),
                ('Short_National', models.IntegerField(blank=True, default='', null=True)),
                ('Junior_National', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Junior_National', models.IntegerField(blank=True, default='', null=True)),
                ('New_Warwick', models.IntegerField(blank=True, default='', null=True)),
                ('Long_Warwick', models.IntegerField(blank=True, default='', null=True)),
                ('Warwick', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Warwick', models.IntegerField(blank=True, default='', null=True)),
                ('Junior_Warwick', models.IntegerField(blank=True, default='', null=True)),
                ('Short_Junior_Warwick', models.IntegerField(blank=True, default='', null=True)),
            ],
            options={
                'ordering': ['handicap'],
            },
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roundname', models.CharField(max_length=200)),
                ('maxscore', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RoundType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rndtype', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('third', models.IntegerField(blank=True, default='', null=True, verbose_name='3rd Class Bowman')),
                ('second', models.IntegerField(blank=True, default='', null=True, verbose_name='2nd Class Bowman')),
                ('first', models.IntegerField(blank=True, default='', null=True, verbose_name='1st Class Bowman')),
                ('BM', models.IntegerField(blank=True, default='', null=True, verbose_name='Bowman')),
                ('MB', models.IntegerField(blank=True, default='', null=True, verbose_name='Master Bowman')),
                ('GMB', models.IntegerField(blank=True, default='', null=True, verbose_name='Grand Master Bowman')),
                ('classindex', models.CharField(max_length=5, null=True)),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shooting', to='score.age')),
                ('bowtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score.bowtype', verbose_name='bows')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roundtype', to='score.roundtype')),
                ('roundname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score.round', verbose_name='round')),
            ],
            options={
                'ordering': ['bowtype', 'age', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1)),
                ('DoB', models.DateField(help_text='Date of Birth must take the form dd/mm/yyyy', null=True, verbose_name='Date of Birth')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
