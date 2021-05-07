from django.db import models

class EntryType(models.Model):
    type = models.CharField(max_length=200)
    created_at = models.DateTimeField('created at')

    def __str__(self):
        return self.type

class Entry(models.Model):
    entry_type = models.ForeignKey(EntryType, on_delete=models.CASCADE)
    value = models.CharField(max_length=254)
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')

    def __str__(self):
        return self.value
