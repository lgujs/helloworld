__author__ = 'Administrator'


from rest_framework import serializers
from apptest.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'created', 'title', 'code', 'linenos')


class UserSerializer(serializers.ModelSerializer):
#    snippets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')