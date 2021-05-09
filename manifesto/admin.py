from django.contrib import admin

from manifesto.models import Entry, EntryType

admin.site.register(EntryType)
admin.site.register(Entry)
