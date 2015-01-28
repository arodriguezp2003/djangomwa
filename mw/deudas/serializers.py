from django.contrib.auth.models import User, Group
from .models import Persona, Deuda
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('url', 'name','email','phone','owner')

class DeudaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deuda
        fields = ('url', 'name','Persona','create', 'price','state','paiddate','paid','owner')