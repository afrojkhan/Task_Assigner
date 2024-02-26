from rest_framework import serializers
from .models import StateMaster

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateMaster
        fields = "__all__"
