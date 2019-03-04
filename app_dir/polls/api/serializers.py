from rest_framework import serializers
from django.contrib.auth import get_user_model

from app_dir.polls.models import Choice

class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'question',
            'choice_text',
            'votes',
            'id',
        ]


