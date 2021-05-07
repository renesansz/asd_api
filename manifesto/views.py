from rest_framework import viewsets
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import IsAuthenticated

from .models import EntryType, Entry
from .serializers import EntryTypeSerializer, EntrySerializer

class EntryViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = EntryType.objects.all()
    serializer_class = EntryTypeSerializer
