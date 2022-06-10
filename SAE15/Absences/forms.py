from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class GroupesForm(ModelForm):
    class Meta:
        model = models.Groupes
        fields = ('nomgroupe',)
        labels = {
            'nomgroupe': _('Nom du groupe')
        }

class EtudiantsForm(ModelForm):
    class Meta:
        model = models.Etudiants
        fields=('nometu', 'prenometu', 'emailetu', 'photoetu', 'groupesetu')
        labels = {
            'nometu' : _("Nom de l'étudiant"),
            'prenometu' : _('Prénom de l\'étudiant'),
            'emailetu' : _('Email de l\'étudiant'),
            'photoetu' : _('Photo de l\'étudiant'),
            'groupesetu' : _('Groupes de l\'étudiant'),
        }

class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('nomens', 'prenomens', 'emailens')
        labels = {
            'nomens' : _('Nom enseignant') ,
            'prenomens' : _('Prénom enseignant'),
            'emailens' : _('e-mail enseignant')
        }

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours
        fields = ('titre_du_cours', 'date', 'enseignant', 'durée', 'groupe')
        labels = {
            'titre_du_cours' : _('Titre du cours') ,
            'date' : _('Date du cours'),
            'enseignant' : _('Enseignant du cours'),
            'durée' : _('Durée du cours'),
            'groupe' : _('Groupe'),
        }

class AbsCoursForm(ModelForm):
    class Meta:
        model = models.AbsCours
        fields = ('cours', 'etudiants', 'justified', 'justificatif',)
        labels = {
            'cours' : _('Cours') ,
            'Etudiants' : _('Etudiants absents'),
            'justified' : _('Justifié'),
            'justificatif' : _('Justificatif'),
        }
