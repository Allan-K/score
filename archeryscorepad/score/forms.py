from django import forms
from .models import ProfileUser, Score, club, roundscore
from django.forms import ModelForm, TextInput
from score.models import ProfileUser, Score, club
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DatePickerInput

class RegistrationForm(UserCreationForm):

    class Meta:
        model = ProfileUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'club',
            'email',
            'gender',
            'DoB',
            'password1',
            'password2',
        )
        widgets = {'DoB': DatePickerInput(format='%d/%m/%Y')}
        help_texts = {
            'password1': None,
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.gender = self.cleaned_data['gender']
        user.DoB = self.cleaned_data['DoB']
        if commit:
            user.save()

        return user


class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = [
            'rndname',
            'bowtype',
            'dateshot',
            'score'
        ]
        widgets = {'dateshot' : DatePickerInput(format='%d/%m/%Y')}

class AddClubForm(forms.ModelForm):
    class Meta:
        model = club
        fields = [
            'club_name',
            'region'
        ]

class AddRoundScore(forms.ModelForm):
    class Meta:
        model = roundscore
        fields = [
            'shot_1',
            'shot_2',
            'shot_3',
            'shot_4',
            'shot_5',
            'shot_6',
            'shot_7',
            'shot_8',
            'shot_9',
            'shot_10',
            'shot_11',
            'shot_12'
        ]
        widgets = {
            'shot_1': TextInput(attrs={'':''}),
            'shot_2': TextInput(attrs={'':''}),
            'shot_3': TextInput(attrs={'':''}),
            'shot_4': TextInput(attrs={'':''}),
            'shot_5': TextInput(attrs={'':''}),
            'shot_6': TextInput(attrs={'':''}),
            'shot_7': TextInput(attrs={'':''}),
            'shot_8': TextInput(attrs={'':''}),
            'shot_9': TextInput(attrs={'':''}),
            'shot_10': TextInput(attrs={'':''}),
            'shot_11': TextInput(attrs={'':''}),
            'shot_12': TextInput(attrs={'':''}),
        }
