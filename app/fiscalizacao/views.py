from app.fiscalizacao.models import Relato
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.fiscalizacao.serializers import RelatoSerializer, UserSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RelatoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Relato.objects.all()
    serializer_class = RelatoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
