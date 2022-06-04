from csv import list_dialects
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models import Sum, Count, Avg
from django.db.models.deletion import CASCADE
from django.utils import timezone
from datetime import datetime

class ProfileUser(AbstractUser):
    GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )
    gender = models.CharField(max_length=1, default="M", choices=GENDER_CHOICES)
    DoB = models.DateField(verbose_name="Date of Birth", null=True, help_text="Date of Birth must take the form dd/mm/yyyy")
    club = models.ForeignKey('club', null=True, blank=True, on_delete=models.CASCADE)

    def calculate_age(self):
        return int((datetime.now().date() - self.DoB).days / 365.25)
    age = property(calculate_age) 

    def calculate_shootingas(self):
        if self.gender == 'F':
            if self.age >= 18:
                return 1
            elif self.age <= 18 and self.age >= 17:
                return 2
            elif self.age <= 16 and self.age >= 15:
                return 3
            elif self.age <= 14 and self.age >= 13 :
                return 4
            elif self.age <= 12:
                return 5
        if self.gender == 'M':
            if self.age >= 18:
                return 6
            elif self.age <= 18 and self.age >= 17:
                return 7
            elif self.age <= 16 and self.age >= 15:
                return 8
            elif self.age <= 14 and self.age >= 13:
                return 9
            elif self.age <= 12:
                return 10
    shooting = property(calculate_shootingas)



class BowType(models.Model) :

    bowtype = models.CharField(max_length=10)

    def __str__(self):
        return str(self.bowtype)

class Round(models.Model):
    roundname = models.CharField(max_length=200)
    maxscore = models.IntegerField(default=0)
    type = models.CharField(max_length=1, default='M')
    numberOfEnds = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.roundname)

#class RoundType(models.Model):
#    rndtype = models.CharField(max_length=7)

#    def __str__(self):
#        return str(self.rndtype)


class Age(models.Model):
    ageband = models.CharField(max_length=14)
    maxage = models.IntegerField(verbose_name="Age Range")
    gender = models.CharField(max_length=1)

    def __str__(self):
        return str(self.ageband)

class Classification(models.Model):
    age = models.ForeignKey('Age', related_name='shooting', on_delete=models.CASCADE)
    bowtype = models.ForeignKey("BowType", verbose_name='bows', on_delete=models.CASCADE) 
    roundname = models.ForeignKey('Round', verbose_name='round', on_delete=models.CASCADE)   
#    round = models.ForeignKey('RoundType', related_name='roundtype', on_delete=models.CASCADE)
    third = models.CharField(max_length=4, verbose_name="3rd Class Bowman", null=True, blank=True)
    second = models.CharField(max_length=4, verbose_name="2nd Class Bowman",  null=True, blank=True)
    first = models.CharField(max_length=4, verbose_name="1st Class Bowman",  null=True, blank=True)
    BM = models.CharField(max_length=4, verbose_name="Bowman",  null=True, blank=True)
    MB = models.CharField(max_length=4, verbose_name="Master Bowman",  null=True, blank=True)
    GMB = models.CharField(max_length=4, verbose_name="Grand Master Bowman",  null=True, blank=True)
    classindex = models.CharField(max_length=5, null=True)

    class Meta:
        ordering = ['bowtype', 'age', 'id']

    def index(self):
        return str(self.age.ageband)+ ' ' +str(self.bowtype.bowtype)+ ' ' +str(self.roundname.roundname)
    index = property(index) 

    def save(self, *args, **kwargs):
       self.classindex = self.index  
       super(Classification, self).save(*args, **kwargs)   

    def __str__(self):
        return self.index + ' ' + str(self.classindex)


class Handicap(models.Model): 
    handicap = models.IntegerField(primary_key=True)
    WA1440_Gents = models.IntegerField(default='', blank=True, null=True)
    WA1440_Ladies = models.IntegerField(default='', blank=True, null=True)
    Half_WA1440_Gents = models.IntegerField(default='', blank=True, null=True)
    Half_WA1440_Ladies = models.IntegerField(default='', blank=True, null=True)
    Metric_I = models.IntegerField(default='', blank=True, null=True)
    Metric_II = models.IntegerField(default='', blank=True, null=True)
    Metric_III = models.IntegerField(default='', blank=True, null=True)
    Metric_IV = models.IntegerField(default='', blank=True, null=True)
    Metric_V = models.IntegerField(default='', blank=True, null=True)
    Long_Metric_Gents = models.IntegerField(default='', blank=True, null=True)
    Long_Metric_Ladies = models.IntegerField(default='', blank=True, null=True)
    Long_Metric_II = models.IntegerField(default='', blank=True, null=True)
    Long_Metric_III = models.IntegerField(default='', blank=True, null=True)
    Long_Metric_IV = models.IntegerField(default='', blank=True, null=True)
    Long_Metric_V = models.IntegerField(default='', blank=True, null=True)
    Short_Metric = models.IntegerField(default='', blank=True, null=True)
    Short_Metric_II = models.IntegerField(default='', blank=True, null=True)
    Short_Metric_III = models.IntegerField(default='', blank=True, null=True)
    Short_Metric_IV = models.IntegerField(default='', blank=True, null=True)
    Short_Metric_V = models.IntegerField(default='', blank=True, null=True)
    WA_900 = models.IntegerField(default='', blank=True, null=True)
    WA_70M = models.IntegerField(default='', blank=True, null=True)
    WA_60M = models.IntegerField(default='', blank=True, null=True)
    WA_50M = models.IntegerField(default='', blank=True, null=True)
    WA_Standard_Bow = models.IntegerField(default='', blank=True, null=True)
    Olympic_Match = models.IntegerField(default='', blank=True, null=True)
    York = models.IntegerField(default='', blank=True, null=True)
    Hereford = models.IntegerField(default='', blank=True, null=True)
    Bristol_II = models.IntegerField(default='', blank=True, null=True)
    Bristol_III = models.IntegerField(default='', blank=True, null=True)
    Bristol_IV = models.IntegerField(default='', blank=True, null=True)
    Bristol_V = models.IntegerField(default='', blank=True, null=True)
    St_George = models.IntegerField(default='', blank=True, null=True)
    Albion = models.IntegerField(default='', blank=True, null=True)
    Windsor = models.IntegerField(default='', blank=True, null=True)
    Short_Windsor = models.IntegerField(default='', blank=True, null=True)
    Junior_Windsor = models.IntegerField(default='', blank=True, null=True)
    Short_Junior_Windsor = models.IntegerField(default='', blank=True, null=True)
    New_Western = models.IntegerField(default='', blank=True, null=True)
    Long_Western = models.IntegerField(default='', blank=True, null=True)
    Western = models.IntegerField(default='', blank=True, null=True)
    Short_Western = models.IntegerField(default='', blank=True, null=True)
    Junior_Western = models.IntegerField(default='', blank=True, null=True)
    Short_Junior_Western = models.IntegerField(default='', blank=True, null=True)
    American = models.IntegerField(default='', blank=True, null=True)
    St_Nicholas = models.IntegerField(default='', blank=True, null=True)
    New_National = models.IntegerField(default='', blank=True, null=True)
    Long_National = models.IntegerField(default='', blank=True, null=True)
    National = models.IntegerField(default='', blank=True, null=True)
    Short_National = models.IntegerField(default='', blank=True, null=True)
    Junior_National = models.IntegerField(default='', blank=True, null=True)
    Short_Junior_National = models.IntegerField(default='', blank=True, null=True)
    New_Warwick = models.IntegerField(default='', blank=True, null=True)
    Long_Warwick = models.IntegerField(default='', blank=True, null=True)
    Warwick = models.IntegerField(default='', blank=True, null=True)
    Short_Warwick = models.IntegerField(default='', blank=True, null=True)
    Junior_Warwick = models.IntegerField(default='', blank=True, null=True)
    Short_Junior_Warwick = models.IntegerField(default='', blank=True, null=True)
 
    class Meta:
        ordering = ['handicap']

    def __str__(self):
        return str(self.handicap) 


class Score(models.Model):
    archer = models.ForeignKey('ProfileUser', on_delete=CASCADE)
    rndname = models.ForeignKey('Round', related_name='round', on_delete=CASCADE)
    shootingas = models.ForeignKey('Age', related_name='shootingas', on_delete=models.CASCADE)
    bowtype = models.ForeignKey('BowType', related_name='bowtypes', default=1, on_delete=CASCADE)
    score = models.IntegerField(default=0, blank=True)
    classification = models.CharField(max_length=6, blank=True, null=True)
    handicap = models.IntegerField(default=0, blank=True, null=True)
    cumulativeHandicap = models.IntegerField(default=0, blank=True, null=True)
    dateshot = models.DateField(verbose_name="Date Round Shot", default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    classid = models.IntegerField(default=0)

    def classify(self):
        z = self.classid
        a = Classification.objects.filter(classindex=self.classid).values_list('third', flat=True).last()
        b = Classification.objects.filter(classindex=self.classid).values_list('second', flat=True).last()
        c = Classification.objects.filter(classindex=self.classid).values_list('first', flat=True).last()
        d = Classification.objects.filter(classindex=self.classid).values_list('BM', flat=True).last()
        e = Classification.objects.filter(classindex=self.classid).values_list('MB', flat=True).last()
        f = Classification.objects.filter(classindex=self.classid).values_list('GMB', flat=True).last()

        if self.score <= int(a) or int(a) == 0:
            return 'N/A'       
        elif self.score >= int(f) and int(f) != 0:
           return 'Grand Master Bowman'
        elif self.score >= int(e) and int(e) != 0:
            return 'Master Bowman'
        elif self.score >= int(d) and int(d) != 0:
            return 'Bowman'
        elif self.score >= int(c) and int(c) != 0:
            return 'First Class'
        elif self.score >= int(b) and int(b) != 0:
            return 'Second Class'
        elif self.score >= int(a) and int(a) != 0:
            return 'Third Class'
            
    classify = property(classify)

    def hcap(self):
        hcap0 = Handicap_Rotated.objects.filter(round_id=self.rndname).values_list()
        list_hcap = [entry for entry in hcap0][0][3:]

        lower = min(list_hcap,key=lambda x : x - self.score > 0 )
        result = list_hcap.index(lower)
        return result
    hcap = property(hcap)

    def comp_hcap(self):
        numberOfRounds = Score.objects.all().filter(archer_id=self.archer).aggregate(Count('score'))
        print('Num Rounds', numberOfRounds)
        length = numberOfRounds['score__count']      
        var = self.hcap
        if length == 2:
            initial = Score.objects.all().filter(archer_id=self.archer).order_by('archer_id')[:3].aggregate(Avg('handicap'))
            print('Initial', initial)
            round_initial = initial['handicap__avg']
            comp_hcap = round_initial
            return comp_hcap
        if length >= 3:
            new_handicap = Score.objects.values().filter(archer_id=self.archer).first()
            new_handicap = new_handicap['cumulativeHandicap']
            print('New Handicap', new_handicap)
            if var == new_handicap:
                comp_hcap = var
                return comp_hcap
            elif var <= new_handicap - 2:
                comp_hcap = int((new_handicap + var) / 2)
                return comp_hcap
            elif var >= new_handicap - 2:
                comp_hcap = int((new_handicap + var) / 2)
                return comp_hcap
            else:
                print('No')
                print('Longer than 3')
            #print('Initial', initial)
        else:
            return 0
            #print('message', 'Not enough rounds shot')
        print('Length', length)
        print('Var', var)
    comp_hcap = property(comp_hcap)

    class Meta:
        ordering = ['-dateshot', '-id']

    def save(self, *args, **kwargs):
       self.cumulativeHandicap = self.comp_hcap  
       self.classification = self.classify
       self.handicap = self.hcap
       super(Score, self).save(*args, **kwargs)  


    def __str__(self):
        return str(self.id )


class club(models.Model):
    REGION_CHOICES = (
        ('-', '----'),
        ('NCAS', 'NCAS'),
        ('EMAS', 'EMAS'),
        ('GCAS', 'GCAS'),
        ('WMAS', 'WMAS'),
        ('SCAS', 'SCAS'),
        ('Ssottish Archery', 'Scottish Archery'),
        ('Welsh Archery', 'Welsh Archery'),
        ('NI Archery', 'Archery NI')
    )
    club_name = models.CharField(max_length=200, default='', blank=True, null=True)
    region = models.CharField(max_length=200, default='----', choices =REGION_CHOICES)

    class Meta:
        ordering = ['club_name']


    def __str__(self):
        return str(self.club_name) + ' - ' + str(self.region)


class Handicap_Rotated(models.Model):
    round = models.ForeignKey('Round', on_delete=CASCADE)
    round_name = models.CharField(default='', max_length=20)
    zero = models.IntegerField(default=0, blank=True, null=True) 
    one = models.IntegerField(default=0, blank=True, null=True)
    two = models.IntegerField(default=0, blank=True, null=True) 
    three = models.IntegerField(default=0, blank=True, null=True)
    four = models.IntegerField(default=0, blank=True, null=True)
    five = models.IntegerField(default=0, blank=True, null=True) 
    six = models.IntegerField(default=0, blank=True, null=True)
    seven = models.IntegerField(default=0, blank=True, null=True)
    eight = models.IntegerField(default=0, blank=True, null=True) 
    nine = models.IntegerField(default=0, blank=True, null=True)
    ten = models.IntegerField(default=0, blank=True, null=True) 
    eleven = models.IntegerField(default=0, blank=True, null=True)
    twelve = models.IntegerField(default=0, blank=True, null=True) 
    thirteen = models.IntegerField(default=0, blank=True, null=True)
    fourteen = models.IntegerField(default=0, blank=True, null=True)
    fifteen = models.IntegerField(default=0, blank=True, null=True) 
    sixteen = models.IntegerField(default=0, blank=True, null=True)
    seventeen = models.IntegerField(default=0, blank=True, null=True)
    eighteen = models.IntegerField(default=0, blank=True, null=True) 
    nineteen = models.IntegerField(default=0, blank=True, null=True)
    twenty = models.IntegerField(default=0, blank=True, null=True) 
    twentyone = models.IntegerField(default=0, blank=True, null=True)
    twentytwo = models.IntegerField(default=0, blank=True, null=True) 
    twentythree = models.IntegerField(default=0, blank=True, null=True)
    twentyfour = models.IntegerField(default=0, blank=True, null=True)
    twentyfive = models.IntegerField(default=0, blank=True, null=True) 
    twentysix = models.IntegerField(default=0, blank=True, null=True)
    twentyseven = models.IntegerField(default=0, blank=True, null=True)
    twentyeight = models.IntegerField(default=0, blank=True, null=True) 
    twentynine = models.IntegerField(default=0, blank=True, null=True)
    thirty = models.IntegerField(default=0, blank=True, null=True) 
    thirtyone = models.IntegerField(default=0, blank=True, null=True)
    thirtytwo = models.IntegerField(default=0, blank=True, null=True) 
    thirtythree = models.IntegerField(default=0, blank=True, null=True)
    thirtyfour = models.IntegerField(default=0, blank=True, null=True)
    thirtyfive = models.IntegerField(default=0, blank=True, null=True) 
    thirtysix = models.IntegerField(default=0, blank=True, null=True)
    thirtyseven = models.IntegerField(default=0, blank=True, null=True)
    thirtyeight = models.IntegerField(default=0, blank=True, null=True) 
    thirtynine = models.IntegerField(default=0, blank=True, null=True)
    forty = models.IntegerField(default=0, blank=True, null=True) 
    fortyone = models.IntegerField(default=0, blank=True, null=True)
    fortytwo = models.IntegerField(default=0, blank=True, null=True) 
    fortythree = models.IntegerField(default=0, blank=True, null=True)
    fortyfour = models.IntegerField(default=0, blank=True, null=True)
    fortyfive = models.IntegerField(default=0, blank=True, null=True) 
    fortysix = models.IntegerField(default=0, blank=True, null=True)
    fortyseven = models.IntegerField(default=0, blank=True, null=True)
    fortyeight = models.IntegerField(default=0, blank=True, null=True) 
    fortynine = models.IntegerField(default=0, blank=True, null=True)
    fifty = models.IntegerField(default=0, blank=True, null=True) 
    fiftyone = models.IntegerField(default=0, blank=True, null=True)
    fiftytwo = models.IntegerField(default=0, blank=True, null=True) 
    fiftythree = models.IntegerField(default=0, blank=True, null=True)
    fiftyfour = models.IntegerField(default=0, blank=True, null=True)
    fiftyfive = models.IntegerField(default=0, blank=True, null=True) 
    fiftysix = models.IntegerField(default=0, blank=True, null=True)
    fiftyseven = models.IntegerField(default=0, blank=True, null=True)
    fiftyeight = models.IntegerField(default=0, blank=True, null=True) 
    fiftynine = models.IntegerField(default=0, blank=True, null=True)
    sixty = models.IntegerField(default=0, blank=True, null=True) 
    sixtyone = models.IntegerField(default=0, blank=True, null=True)
    sixtytwo = models.IntegerField(default=0, blank=True, null=True) 
    sixtythree = models.IntegerField(default=0, blank=True, null=True)
    sixtyfour = models.IntegerField(default=0, blank=True, null=True)
    sixtyfive = models.IntegerField(default=0, blank=True, null=True) 
    sixtysix = models.IntegerField(default=0, blank=True, null=True)
    sixtyseven = models.IntegerField(default=0, blank=True, null=True)
    sixtyeight = models.IntegerField(default=0, blank=True, null=True) 
    sixtynine = models.IntegerField(default=0, blank=True, null=True)
    seventy = models.IntegerField(default=0, blank=True, null=True) 
    seventyone = models.IntegerField(default=0, blank=True, null=True)
    seventytwo = models.IntegerField(default=0, blank=True, null=True) 
    seventythree = models.IntegerField(default=0, blank=True, null=True)
    seventyfour = models.IntegerField(default=0, blank=True, null=True)
    seventyfive = models.IntegerField(default=0, blank=True, null=True) 
    seventysix = models.IntegerField(default=0, blank=True, null=True)
    seventyseven = models.IntegerField(default=0, blank=True, null=True)
    seventyeight = models.IntegerField(default=0, blank=True, null=True) 
    seventynine = models.IntegerField(default=0, blank=True, null=True)
    eighty = models.IntegerField(default=0, blank=True, null=True) 
    eightyone = models.IntegerField(default=0, blank=True, null=True)
    eightytwo = models.IntegerField(default=0, blank=True, null=True) 
    eightythree = models.IntegerField(default=0, blank=True, null=True)
    eightyfour = models.IntegerField(default=0, blank=True, null=True)
    eightyfive = models.IntegerField(default=0, blank=True, null=True) 
    eightysix = models.IntegerField(default=0, blank=True, null=True)
    eightyseven = models.IntegerField(default=0, blank=True, null=True)
    eightyeight = models.IntegerField(default=0, blank=True, null=True) 
    eightynine = models.IntegerField(default=0, blank=True, null=True)
    ninety = models.IntegerField(default=0, blank=True, null=True) 
    ninetyone = models.IntegerField(default=0, blank=True, null=True)
    ninetytwo = models.IntegerField(default=0, blank=True, null=True) 
    ninetythree = models.IntegerField(default=0, blank=True, null=True)
    eleven = models.IntegerField(default=0, blank=True, null=True)
    ninetyfour = models.IntegerField(default=0, blank=True, null=True)
    ninetyfive = models.IntegerField(default=0, blank=True, null=True) 
    ninetysix = models.IntegerField(default=0, blank=True, null=True)
    ninetyseven = models.IntegerField(default=0, blank=True, null=True)
    ninetyeight = models.IntegerField(default=0, blank=True, null=True) 
    ninetynine = models.IntegerField(default=0, blank=True, null=True)
    onehundred = models.IntegerField(default=0, blank=True, null=True)
    pass

class roundscore(models.Model):
    scoreid = models.IntegerField(default=0, blank=True, null=True)
    end_count = models.IntegerField(default=0)
    #scoreid = models.ForeignKey('Score', on_delete=CASCADE)
    shot_1 = models.IntegerField(default=0, validators=[MaxValueValidator (10)],blank=True, null=True)
    shot_2 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    shot_3 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    shot_4 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    shot_5 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    shot_6 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    end_1 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    end_1_counter = models.IntegerField(default=0)
    shot_7 = models.IntegerField(default=0, validators=[MaxValueValidator (10)],blank=True, null=True)
    shot_8 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    shot_9 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    shot_10 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    shot_11 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    shot_12 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    end_2 = models.IntegerField(default=0, validators=[MaxValueValidator (10)], blank=True, null=True)
    end_2_counter = models.IntegerField(default=0)    
    tens = models.IntegerField(default=0, blank=True, null=True)
    doz = models.IntegerField(default = 0, null=True)
    distance_score = models.IntegerField(default=0, null=True)

    def end_1_counter_calc(self):
        end1Counter_result = self.end_count + self.end_count - 1
        return end1Counter_result
    end_1_counter_calc = property(end_1_counter_calc)

    def end_2_counter_calc(self):
        end2Counter_result = self.end_count + self.end_count
        return end2Counter_result
    end_2_counter_calc = property(end_2_counter_calc)

    def end_1_calc(self):
        end_1_result = self.shot_1 + self.shot_2 + self.shot_3 + self.shot_4 + self.shot_5 + self.shot_6
        return end_1_result
    end_1_calc = property(end_1_calc)

    def end_2_calc(self):
        end_2_result = self.shot_7 + self.shot_8 + self.shot_9 + self.shot_10 + self.shot_11 + self.shot_12
        return end_2_result
    end_2_calc = property(end_2_calc)

    def doz_calc(self):
        doz_result = self.end_1 + self.end_2
        return doz_result
    doz_calc = property(doz_calc)

#    def distance_total_calc(self):
#        result1 = 0
#        result2 = 0
#        result3 = 0
#        if self.end_count == 1:
#            result1 = self.doz
#            print(result1)
#        if self.end_count == 2:
#            result2 = self.doz + result1
#            print(result1)
#        if self.end_count == 3:
#            result3 = self.doz + result2
#            print(result3)
#    distance_total_calc = property(distance_total_calc)


    def tens_calc(self):
        result =0 
        if self.shot_1 == 10:
            result += 1
        if self.shot_2 == 10:
            result += 1
        if self.shot_3 == 10:
            result += 1
        if self.shot_4 == 10:
            result += 1
        if self.shot_5 == 10:
            result += 1
        if self.shot_6 == 10:
            result += 1 
        if self.shot_7 == 10:
            result += 1
        if self.shot_8 == 10:
            result += 1
        if self.shot_9 == 10:
            result += 1
        if self.shot_10 == 10:
            result += 1
        if self.shot_11 == 10:
            result += 1
        if self.shot_12 == 10:
            result += 1 
        return result
    tens_calc = property(tens_calc)

    def __str__(self):
        return str(self.scoreid)

    def save(self, *args, **kwargs):
        self.end_1 = self.end_1_calc 
        self.end_2 = self.end_2_calc 
        self.tens = self.tens_calc
        self.doz = self.doz_calc
#        self.distance_score = self.distance_total_calc
        self.end_1_counter = self.end_1_counter_calc
        self.end_2_counter = self.end_2_counter_calc
        super(roundscore, self).save(*args, **kwargs)