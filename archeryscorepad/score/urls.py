from django.urls import path
from score import views

app_name = 'score'

urlpatterns=[
    path("", views.index, name="index"),
    path("registration", views.registration, name="registration"),      
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("myprofile/<int:id>", views.myprofile, name="myprofile"), 
    path("registration/<int:pk>/edit/", views.edit_profile, name='edit_profile'),  
    path("round/<int:id>", views.round, name="round"), 
    path("addscore", views.addscore, name="addscore"),
    path("clubscores/<int:id>", views.clubscores, name="clubscores"),    
    path("roundscores", views.roundscores, name="roundscores"),
    path("displayroundscores/<int:id>", views.displayroundscores, name="displayroundscores"),
    path("scores/<int:id>", views.scores, name="scores"),
    path("myscores/<int:id>", views.myscores, name="myscores"),
    path("addaclub", views.addaclub, name="addaclub"),
    path("addscorecard/<int:pk>", views.addscorecard, name="addscorecard"),
    #path("addscorecard", views.addscorecard, name="addscorecard"),
    path("readscorecard/<int:id>", views.readscorecard, name="readscorecard"),
]