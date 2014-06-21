from app.fiscalizacao.models import Relato
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.fiscalizacao.serializers import RelatoSerializer, UserSerializer

from rest_framework import generics

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from permissions import IsOwnerOrAdmin

class RelatoViewSet(viewsets.ModelViewSet):
    queryset = Relato.objects.all()
    serializer_class = RelatoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

#class UserList(generics.ListAPIView):

#    serializer_class = UserSerializer

#    def get_queryset(self):
#        user = self.request.user
#        return User.objects.all()

class UserViewSet(generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAdminUser,IsAuthenticatedOrReadOnly)

    #def pre_save(self, obj):
    #    pass

#    def get_queryset(self):
#        user = self.request.user
#        return User.objects.all()