from django.contrib import admin

from .models import Entry, EntryType

admin.site.register(EntryType)
admin.site.register(Entry)
