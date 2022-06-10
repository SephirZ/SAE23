from django.db import models

# Create your models here.
class Groupes(models.Model):
    nomgroupe = models.CharField(max_length=100) #eeeeeeesqfsfs cougre

    def __str__(self):
        chaine = f" Groupe : '{self.nomgroupe}'"
        return chaine

    def dico(self):
        return {"nomgroupe": self.nomgroupe}


class Etudiants(models.Model):
    nometu = models.CharField(max_length=100)
    prenometu = models.CharField(max_length=100)
    emailetu = models.CharField(max_length=50)
    photoetu = models.TextField(null = True, blank = True)
    groupesetu = models.ForeignKey("groupes", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.nometu} {self.prenometu}. Adresse mail :  {self.emailetu}, Photo : {self.photoetu}, Groupe : {self.groupesetu}"
        return chaine

    def dico(self):
        return {"nometu": self.nometu, "prenometu": self.prenometu,"emailetu": self.emailetu, "photoetu": self.photoetu, "groupesetu":self.groupesetu}

class Enseignant(models.Model):
    nomens = models.CharField(max_length = 100)
    prenomens = models.CharField(max_length = 100)
    emailens = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.nomens} {self.prenomens}"
        return chaine

    def dico(self):
        return {"nomens": self.nomens, "prenomens": self.prenomens,"emailens": self.emailens}


class Cours(models.Model):
    titre_du_cours = models.CharField(max_length = 100)
    date = models.DateField(blank=True, null = True)
    enseignant = models.ForeignKey("enseignant", on_delete=models.CASCADE, default=None)
    durée = models.CharField(max_length = 10)
    groupe = models.ForeignKey("groupes", on_delete=models.CASCADE, default=None)


    def __str__(self):
        chaine = f"Titre :{self.titre_du_cours} Date : {self.date}. Enseignant :  {self.enseignant}, durée : {self.durée}, Groupe : {self.groupe}"
        return chaine

    def dico(self):
        return {"Titre du cours": self.titre_du_cours, "Date du cours": self.date,"Enseignant du cours": self.enseignant, "Durée du cours": self.durée, "Groupe": self.groupe}

class AbsCours(models.Model):
    cours = models.ForeignKey("cours", on_delete=models.CASCADE, default=None)
    etudiants = models.ManyToManyField(Etudiants, blank=False)
    justified = models.BooleanField()
    justificatif = models.TextField(null = True, blank=True)


    def __str__(self):
        chaine = f"Cours : {self.cours} Etudiants absents : {self.etudiants}. justifié :  {self.justified}, justificatif : {self.justificatif}"
        return chaine

    def dico(self):
        return {"cours": self.cours, "etudiants": self.etudiants,"justified": self.justified, "justificatif": self.justificatif}