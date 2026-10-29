from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

    
class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=150)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.PROTECT,
        related_name="livres",
    )
    def __str__(self):
        return self.titre