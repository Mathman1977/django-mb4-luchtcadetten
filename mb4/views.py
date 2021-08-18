from django.shortcuts import render
from django.views import generic
from .models import Reeks, Opgave,Oefening
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import datetime
from datetime import datetime
import time
from PIL import Image



# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     context_object_name = 'laatste_reeksen'

#     def get_queryset(self):
#         # geeft alle reeksen weer
#         return Reeks.objects.all()

def index(request):
    laatste_oef_lijst = Reeks.objects.order_by('-datum')[:5]
    context = {'laatste_oef_lijst': laatste_oef_lijst,'title':'overzicht'}
    return render(request, 'mb4/index.html', context)

# moet nog een detailpagina over de oefening komen
def detail(request, reeks_id):
    reeks = get_object_or_404(Reeks, pk=reeks_id)
    index = 1
    return render(request, 'mb4/detail.html', {'title': reeks.titel, 'reeks': reeks, 'index': index})

juist =[]
fouten = []
slowmo = []

def training(request):
    datum_gemaakt = datetime.now()
    reeks = get_object_or_404(Reeks, pk=1)
    start = round(time.time(), )
    opgaven = reeks.opgave_set.all()
    aantal = opgaven.count()
    opgave = opgaven.first()
    if request.method == "POST":
        jouw_antwoord = request.POST['jouw_antwoord']
        vorige_start = int(request.POST['start'])
        vorige_id = int(request.POST['vorige_id'])
        if jouw_antwoord == "":
            foutmelding = "hey, je moet wel iets kiezen hé!"
            color = 'warning'
            start = vorige_start
            opgave = opgaven.get(pk=vorige_id)
            return render(request, 'mb4/training.html',
                {'title': 'Helaba','reeks': reeks, 'foutmelding': foutmelding, 'opgave': opgave,'color':color,'start': start,'aantal':aantal})
        jouw_antwoord = int(request.POST['jouw_antwoord'])

        # start = datetime.now().time() # is eigenlijk het einde van de vorige oefening
        start = round(time.time(), )
        delta = start - vorige_start
        oef = Oefening(student= request.user,opgave=opgave,antwoord=jouw_antwoord,delta=delta,oef_datum=datum_gemaakt)
        oef.save()



        print(f'vorid {vorige_id}')
        print(f'opgid {opgave.id}')

        vorige_opgave = opgaven.get(pk=vorige_id)
        if oef.antwoord != vorige_opgave.opl:
            fouten.append(vorige_id)
        if oef.delta > vorige_opgave.strtijd:
            slowmo.append(vorige_id)
        if vorige_id < aantal:
            opgave = opgaven.get(pk=vorige_id+1)
            return render(request, 'mb4/training.html',
                {'title': 'Training','reeks': reeks, 'opgave': opgave, 'start': start, 'aantal':aantal})
        else:
            set_fouten = set(fouten)
            aantal_fouten = len(set(fouten))
            aantal_juist = aantal - aantal_fouten
            return render(request, 'mb4/resultaten.html',
                {'title': 'Training','reeks': reeks, 'opgave': opgave,
                'fouten': fouten, 'slowmo': slowmo,'aantal':aantal,
                'aantal_fouten':aantal_fouten, 'aantal_juist': aantal_juist})

    return render(request, 'mb4/training.html',
        {'title': 'Training','reeks': reeks, 'opgave': opgave, 'start': start,'aantal':aantal})


def resultaten(request):

    reeks = get_object_or_404(Reeks, pk=1)
    # opgaven = reeks.opgave_set.all()
    # oefeningen = Oefening.objects.filter(student=request.user)
    # for oef in oefeningen:
    #     print(oef.antwoord)
    # juist_lijst = [1,2,3]
    # fouten = [1, 2, 3]
    # slowmo = [1, 2, 3]
    # # for opgave in opgaven_lijst:
    # #     if antw[1] != juist_lijst[1]:
    # #         fouten.append(antw)
    # #     elif antw[2] > juist_lijst[2]:
    # #         slowmo.append(antw)
    return render(request, 'mb4/resultaten.html', {'title': 'Goe Gedaan','reeks': reeks, 'fouten': fouten, 'slowmo': slowmo})

def uitgewerkt(request, opg_id):
    opgave = get_object_or_404(Opgave, pk=opg_id)
    title= 'uitgewerkte oefening'
    return render(request, 'mb4/uitgewerkt.html', {'title': title, 'opgave': opgave})


# vraagt de user om zijn favoriete nummer
def fav(request,*args,**kwargs):
    return render(request, "mb4/fav.html",{'title':'favoriet nummer'})

# als je de user 5 geeft, zal de website iedere keer dat je duwt, één aftrekken (5,4,3,2,1, Happy New Year!!!)
def fav_aft(request,*args,**kwargs):
    if request.method == "POST":
        num = int(request.POST['num'])
        return render(request, "mb4/fav_aft.html",{'title': 'Aftellen kan beginnen!','num':num})
    return render(request, "mb4/fav_aft.html",{'title': 'Aftellen kan beginnen!'})

