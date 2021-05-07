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

    def get_queryset(self):
        queryset = Entry.objects.all()
        type = self.request.query_params.get('type')
        if type is not None:
            queryset = queryset.filter(entry_type__id=type)
        return queryset

class EntryTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = EntryType.objects.all()
    serializer_class = EntryTypeSerializer
