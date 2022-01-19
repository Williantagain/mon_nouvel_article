# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Articles(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre = models.CharField(max_length=25)
    commentaire = models.TextField(max_length=50)  # essaie avec models.CharField
    texte = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    date_publication = models.DateTimeField(blank=True, null=True)


    def publication(self):
        self.date_publication = timezone.now()
        self.save()



    def __str__(self):
        return self.commentaire
        return self.titre



