from rest_framework import serializers
from .models import Signup


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signup
        fields = "__all__"