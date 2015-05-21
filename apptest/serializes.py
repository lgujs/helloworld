__author__ = 'Administrator'

from django.forms import widgets
from rest_framework import serializers
from apptest.models import Snippet


class SnippetSerializer(serializers.Serializer):
    pk = serializers.ReadOnlyField()
    title = serializers.CharField(required=False, max_length=100)
    code = serializers.CharField(max_length=100000)
    linenos = serializers.BooleanField(required=False)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.title = attrs['title']
            instance.code = attrs['code']
            instance.linenos = attrs['linenos']
            return instance

        return Snippet(**attrs)