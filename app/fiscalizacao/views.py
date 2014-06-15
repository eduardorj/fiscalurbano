from app.fiscalizacao.models import Relato
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.fiscalizacao.serializers import RelatoSerializer


from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from app.fiscalizacao.permissions import IsOwnerOrReadOnly

class RelatoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Relato.objects.all()
    serializer_class = RelatoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
