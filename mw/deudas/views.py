from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, PersonaSerializer , DeudaSerializer
from .models import Deuda, Persona


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Personas to be viewed or edited.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class DeudaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Deudas to be viewed or edited.
    """
    queryset = Deuda.objects.all()
    serializer_class = DeudaSerializer