from django.utils import timezone

from rest_framework import serializers

from manifesto.models import EntryType, Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        today = timezone.now()
        entry = Entry.objects.create(**validated_data, created_at=today, updated_at=today)
        return entry

class EntryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryType
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
