from django.shortcuts import render
from . forms import GroupesForm
from . import models
from django.http import HttpResponseRedirect
# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = GroupesForm(request)
        if form.is_valid():
            groupe = form.save()
            return render(request,"Absences/affiche.html",{"Groupe" : groupe})
        else:
            return render(request,"Absences/ajout.html",{"form": form})
    else:
        form = GroupesForm()
        return render(request,"Absences/ajout.html",{"form" : form})

def traitement(request):
    gform = GroupesForm(request.POST)
    if gform.is_valid():
        groupe=gform.save()
        return HttpResponseRedirect("/Absences/")
    else:
        return render(request, 'Absences/ajout.html', {'form':gform})

def index(request):
    gList = list(models.Groupes.objects.all())
    return render(request, "Absences/index.html", {"Liste": gList})

def affiche(request, id):
    groupe=models.Groupes.objects.get(pk=id)
    return render(request, "Absences/affiche.html", {"Groupe":groupe})

def update(request, id):
    groupe=models.Groupes.objects.get(pk=id)
    gform = GroupesForm(groupe.dico())
    return render(request, 'Absences/update.html', {"form":gform, "id":id})

def delete(request, id):
    groupe = models.Groupes.objects.get(pk=id)
    groupe.delete()
    return HttpResponseRedirect("/Absences/")

def traitementupdate(request, id):
    gform=GroupesForm(request.POST)
    if gform.is_valid():
        groupe = gform.save(commit=False)
        groupe.id=id;
        groupe.save()
        return HttpResponseRedirect('/Absences/')
    else:
        return render(request, "Absences/update.html", {"form":gform, "id":id})