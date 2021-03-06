# This Python file uses the following encoding: utf-8
from django.db import models
from aula.apps.alumnes.models import Grup

class Grup2Aula(models.Model):
    grup_esfera =  models.CharField(max_length=60, unique=True, blank=True)
    Grup2Aula = models.ForeignKey(Grup, null=True, related_name="grup2aulaesfera_set")
    class Meta:
        ordering = ['Grup2Aula','grup_esfera']
        verbose_name = u'Mapeig Grup Aula Esfera'
        verbose_name_plural = u'Mapejos Grups Aula Esfera'
    def __unicode__(self):
        grup = unicode( self.Grup2Aula) if self.Grup2Aula else u'Sense assignar'
        return  unicode( self.grup_esfera) + ' -> ' + grup

class ParametreEsfera(models.Model):
    nom_parametre =  models.CharField(max_length=45, unique=True, help_text=u'Nom Paràmetre')
    valor_parametre = models.CharField(max_length=240, blank=True)
    class Meta:
        ordering = ['nom_parametre']
        verbose_name = u'Paràmetre Esfera'
        verbose_name_plural = u'Paràmetres Esfera'
    def __unicode__(self):
        return  unicode( self.nom_parametre ) + ': ' + self.valor_parametre[0:10] + '...'

