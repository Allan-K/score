from django.contrib import admin
from .models import Handicap_Rotated, ProfileUser, BowType, Round, Age, Classification, Handicap, Score, club, roundscore

# Register your models here.
admin.site.register(ProfileUser)
admin.site.register(BowType)
admin.site.register(Round)
admin.site.register(Age)
admin.site.register(Classification)
admin.site.register(Handicap)
admin.site.register(Handicap_Rotated)
admin.site.register(Score)
admin.site.register(club)
admin.site.register(roundscore)