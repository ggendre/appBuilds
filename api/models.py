# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
#import settings

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Profile(models.Model):
    user = models.OneToOneField(User) #on étends la classe user de django
    team = models.ForeignKey('Team', blank=True, null=True, on_delete=models.SET_NULL)
    phoneNumber = models.CharField(max_length=45, blank=True)
    accountEnabled    = models.BooleanField(default=True)
    accountCreationSecretKey = models.CharField(max_length=45, blank=True)

    apps = models.ManyToManyField('App', blank=True, null=True)

    def __unicode__(self):
        fullname=self.user.get_full_name();
        if fullname == "":
            return self.user.username
        return fullname

    class Meta:
        ordering = ["user__username"]


class App(models.Model):
    name = models.CharField(max_length=90)
    technicalName = models.CharField(max_length=90, blank=True)

    def __unicode__(self):
        return self.name

    def get_dict(self):
        return dict(
            name = self.name,
            technicalName = self.technicalName
        )

    class Meta:
        ordering = ["name"]


class Build(models.Model):
    app = models.ForeignKey('App')
    os = models.ForeignKey('Os')
    
    bundleName = models.CharField(max_length=90, blank=True, null=True)
    versionNumber    = models.CharField(max_length=10)
    creationDate    = models.DateTimeField()
    
#    buildPath        = models.CharField(max_length=75, blank=True, null=True)
#    emailAppUrl     = models.CharField(max_length=75, blank=True, null=True)
#    iconPath        = models.CharField(max_length=75, blank=True, null=True)

    def __unicode__(self):
        return self.app.name+" "+self.versionNumber

    def get_dict(self):
        return dict(
            #app = dict(
            #    id = self.app.pk,
            #    name = self.app.name
            #),
            versionNumber = self.versionNumber,
            creationDate = self.creationDate
        )

    def os_list(self):
        return ", ".join([os.name for os in self.os.all()])

    class Meta:
        ordering = ["app__name", "-versionNumber"]



class Os(models.Model):
    name = models.CharField(max_length=45, null=True, blank=True)
    technicalName = models.CharField(max_length=45)

    def __unicode__(self):
        if self.name != "":
            return self.name
        return self.technicalName

    def get_dict(self):
        return dict(
            technicalName = self.technicalName,
            name = self.name,
        )
