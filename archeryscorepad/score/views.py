#from msilib.schema import Class
from itertools import count
from collections import defaultdict
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import models
from django.db.models import Count, Min, Max, Avg, Sum
from score.forms import AddClubForm, RegistrationForm, ScoreForm, AddClubForm, AddRoundScore
from score.models import ProfileUser, Round, Classification, Age, BowType, Score, Handicap_Rotated, club, roundscore

def index(request):
    return render(request, 'score/index.html')

def addscore(request):
    if request.method == 'POST':    #calcHC = Score.objects.all().values_list('handicap').filter(archer_id=id)
        form = ScoreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.archer = request.user 
            post.shootingas_id = request.user.shooting 
            post.classid = str(post.shootingas.id) + str(post.bowtype_id) + str(post.rndname.id)
            maxscore = get_object_or_404(Round, roundname=post.rndname)
            mscore = maxscore.maxscore

            if post.score >= mscore:
                message = True
                form = ScoreForm()
                return render(request,  "score/addscore.html", {'form': form, 'message': message})
            else:
                message = False
                post.save()
            return HttpResponseRedirect('/')
    else:
        form = ScoreForm()
        return render(request, 'score/addscore.html', {'form' : form})

    pass

def clubscores(request, id):
    users = ProfileUser.objects.filter(club_id=id).values('club_id__club_name')[0:1]
    posts = Score.objects.values('score', 'archer_id__username', 'bowtype_id__bowtype', 'archer', 'rndname__roundname', 'dateshot').filter(archer_id__club_id=id).order_by('-created_date')
    return render(request, "score/clubscores.html", {'posts': posts, 'users': users})

def myscores(request, id):
    user = ProfileUser.objects.filter(id=id)
    score = Score.objects.all()
    roundscores = roundscore.objects.all()
    classification = Classification.objects.all().values_list('classindex').filter(roundname_id=id)
    return render(request, "score/myscores.html", {'score' : score, 'classification' : classification, 'roundscores': roundscores })

def roundscores(request):
    names = Score.objects.values('rndname__roundname', 'rndname__id').order_by('rndname__id').annotate(archer=Min('rndname'))
    return render(request, "score/roundscores.html", {'names': names})

def displayroundscores(request, id):
    posts = Score.objects.filter(rndname_id=id).order_by('-created_date')
    return render(request,"score/displayroundscores.html", {'posts': posts})

def round(request, id):
    posts = Score.objects.filter(rndname_id=id)
    names = Score.objects.filter(rndname_id=id)[:1]
    index = Score.objects.values('archer_id', 'rndname_id').filter(archer_id=id)
    return render(request, "score/round.html", {'posts': posts, 'names': names})


def myprofile(request, id):
    #user = ProfileUser.objects.get(id=id)
    rnds = Age.objects.values('id','ageband')
    posts = Score.objects.values('rndname__roundname', 'rndname__id').filter(archer_id=id).order_by('rndname').annotate(Count('rndname'))
    cumHcap = Score.objects.values('cumulativeHandicap').filter(archer_id=id).order_by('rndname')
    result = Score.objects.values('classification').filter(archer_id=id).annotate(count=Count('classification')).order_by('classification')
    classification = 'Unclassified'
    for entry in result:
        if entry['classification'] == 'Grand Master Bowman' and entry['count'] >= 3:
            classification = 'Grand Master Bowman'
        elif entry['classification'] == 'Master Bowman' and entry['count'] >= 3:
            classification = 'Master Bowman'
        elif entry['count'] >= 3 and entry['classification'] == 'Bowman':
            classification = 'Bowman'
        elif entry['count'] >= 3 and entry['classification'] == 'First Class':
            classification = 'First Class'
        elif entry['count'] >= 3 and entry['classification'] == 'Second Class':
            classification = 'Second Class'
        elif entry['count'] >= 3 and entry['classification'] == 'Third Class':
            classification = 'Third Class'
        else: 

            print(classification)
    return render(request, 'score/myprofile.html', {'rnds' : rnds, 'posts' : posts, 'cumHcap': cumHcap, 'classification': classification})

def edit_profile(request, pk):
        post = get_object_or_404(ProfileUser, pk=pk)
        if request.method == 'POST':
            form = RegistrationForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                #login(request, user)

                return redirect("registration", pk = post.pk)
        else:
            form= RegistrationForm(instance=post)
        return render(request, 'score/registration.html', {'form': form, 'post': post})

def scores(request, id):
    user = ProfileUser.objects.filter(id=id)
    score = Score.objects.all().filter(rndname_id=id)
    classification = Classification.objects.all().values_list('classindex').filter(roundname_id=id)

    return render(request, "score/scores.html", {'score' : score, 'classification' : classification })

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            #return HttpResponseRedirect(reverse("index"))
            return render(request, "score/index.html")
        else:
            return render(request, "score/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "score/login.html")

def logout_view(request):
    logout(request)
    return render(request, "score/index.html")

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #login(request, user)

            return redirect("/")
    else:
        form= RegistrationForm()
    return render(request, 'score/registration.html', {'form': form})

def addaclub(request):
    clubs = club.objects.all()
    if request.method == 'POST':
        form = AddClubForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddClubForm()
            return render(request, "score/addaclub.html", {'form': form, 'clubs': clubs})
    else:
        form = AddClubForm()
        return render(request, 'score/addaclub.html', {'form': form, 'clubs': clubs})


def addscorecard (request, pk):
    posts = get_object_or_404(Score, pk=pk)
    post = Score.objects.values('id', 'rndname__roundname').filter(id = pk)
    endCount = roundscore.objects.values('scoreid').filter(scoreid=pk).count()
    roundMax = Score.objects.values_list('rndname__numberOfEnds').filter(id=pk)
    user = Score.objects.values('archer_id', 'id').filter(id=pk)
    print('User', user)
    if request.method == 'POST':        
        form = AddRoundScore(request.POST, initial={'scoreid': posts})
        if form.is_valid():
            post = form.save(commit=False)
            post.scoreid = pk
            post.end_count = endCount+1
            post.save()
            return render(request, 'score/index.html' )
        else:
            print (form.errors)

    else:
        form = AddRoundScore()
    return render(request, 'score/addscorecard.html', {'form': form, 'posts': posts, 'post': post, 'endCount': endCount+1})


def readscorecard(request, id):
    readscorecard = roundscore.objects.values().filter(scoreid=id)
    round = Score.objects.values('archer_id', 'id', 'rndname__roundname', 'dateshot').filter(id=id)
    print('Round', round)
    roundcount = readscorecard.count()

    if roundcount == 0 :
        message = True
        return render(request, 'score/readscorecard.html', { 'readscorecard': readscorecard, 'message': message, 'round': round })

    return render(request, 'score/readscorecard.html', {'readscorecard': readscorecard, 'round': round })
    pass   