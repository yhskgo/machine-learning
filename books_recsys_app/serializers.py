from books_recsys_app.models import UserProfile
from rest_framework import serializers

class UsersSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('name', 'arrayratedmoviesindxs', 'lastrecs')