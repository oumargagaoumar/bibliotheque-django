from django.shortcuts import render
from .models import Livre


def accueil(request):
    livres = Livre.objects.select_related("categorie").order_by("titre")
    contexte = {
        "nom_bibliotheque": "Bibliothèque des étudiants",
        "livres": livres,
}
    return render(request, "mon_app/accueil.html", contexte)

def a_propos(request):
    return render(request, "mon_app/a_propos.html")