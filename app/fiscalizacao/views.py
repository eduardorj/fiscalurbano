from app.fiscalizacao.models import Relato
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.fiscalizacao.serializers import RelatoSerializer


from rest_framework import generics
#from rest_framework.permissions import IsAdminUser
from fiscalizacao.permissions import IsOwnerOrReadOnly

#class RelatoViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = Relato.objects.all()
#    serializer_class = RelatoSerializer

class RelatoList(generics.ListCreateAPIView):
    queryset = Relato.objects.all()
    serializer_class = RelatoSerializer
    #permission_classes = (IsAdminUser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_paginate_by(self):
        """
        Use smaller pagination for HTML representations.
        """
        #if self.request.accepted_renderer.format == 'html':
        #    return 100
        return 100