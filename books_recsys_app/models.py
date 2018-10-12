import jsonfield
import numpy as np
import django.db
from django.contrib.auth.models import User
from rest_framework.utils import json


# Create your models here.
class UserProfile(django.db.models.Model):
    user = django.db.models.ForeignKey(User, on_delete=django.db.models.CASCADE, )
    array = jsonfield.JSONField()
    arrayratedmoviesindxs = jsonfield.JSONField()
    lastrecs = jsonfield.JSONField()

    def __unicode__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        create = kwargs.pop('create', None)
        recsvec = kwargs.pop('recsvec', None)
        print('create:', create)
        if create==True:
            super(UserProfile, self).save(*args, **kwargs)
        elif recsvec!=None:
            self.lastrecs = json.dumps(recsvec.tolist())
            super(UserProfile, self).save(*args, **kwargs)
        else:
            nmovies = MovieData.objects.count()
            array = np.zeros(nmovies)
            ratedmovies = self.ratedmovies.all()
            self.arrayratedmoviesindxs = json.dumps([m.movieindx for m in ratedmovies])
            for m in ratedmovies:
                array[m.movieindx] = m.value
            self.array = json.dumps(array.tolist())
            super(UserProfile, self).save(*args, **kwargs)

class MovieRated(django.db.models.Model):
    user = django.db.models.ForeignKey(UserProfile, related_name='ratedmovies', on_delete=django.db.models.CASCADE, )
    movie = django.db.models.CharField(max_length=100)
    movieindx = django.db.models.IntegerField(default=-1)
    value = django.db.models.IntegerField()

class MovieData(django.db.models.Model):
    title = django.db.models.CharField(max_length=100)
    array = jsonfield.JSONField()
    ndim = django.db.models.IntegerField(default=300)
    description = django.db.models.TextField()