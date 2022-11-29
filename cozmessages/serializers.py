from rest_framework import serializers
from .models import Cozmessage

class CozmessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cozmessage
        fields = "__all__"