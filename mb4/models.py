from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Reeks(models.Model):
    titel = models.CharField(max_length=100)
    foto = models.ImageField(blank=True, null=True)
    uitleg = models.TextField()
    datum = models.DateTimeField(default=timezone.now)
    soort =  models.CharField(max_length=100)
    glob_moeilkhgr = models.IntegerField()
    # glob_moeilkhgr = models.TextChoices('stars', '* ** ***')
    glob_strtijd = models.IntegerField()
    vereiste_level = models.CharField(max_length=50)

    class Meta:
        verbose_name = ('Reeks')
        verbose_name_plural =('Reeksen')
        # ordering = ('datum')

    def __str__(self):
        return self.titel

class Opgave(models.Model):
    reeks = models.ForeignKey(Reeks, on_delete=models.CASCADE)
    onderwerp =  models.CharField(max_length=100)
    opg_titel = models.CharField(max_length=100,blank=True)
    opg_foto = models.ImageField(blank=True, null=True)
    opl_foto = models.ImageField(blank=True, null=True)
    opl = models.IntegerField()
    moeilkhgr = models.IntegerField()
    # moeilkhgr = models.TextChoices('stars', '* ** ***')
    strtijd = models.IntegerField()

    class Meta:
        verbose_name = ('Opgave')
        verbose_name_plural =('Opgaven')
        # ordering = ('datum')

    def __str__(self):
        return 'Opgave' + str(self.id)

    # def get_absolute_url(self):
    #     return reverse ('opg-detail', kwargs={'pk':self.pk})

class Oefening(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    opgave = models.ForeignKey(Opgave, on_delete=models.CASCADE)
    antwoord = models.IntegerField(blank=True)
    delta = models.IntegerField()
    oef_datum = models.DateTimeField('datum_gemaakt')

    # def __str__(self):
    #     return self.student + self.opgave.id

    class Meta:
        verbose_name = ('Oefening')
        verbose_name_plural =('Oefeningen')
        # ordering = ('datum')

