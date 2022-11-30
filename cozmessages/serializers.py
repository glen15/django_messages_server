from rest_framework import serializers
from .models import Cozmessage, Submit

class CozmessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cozmessage
        fields = "__all__"

class SubmitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submit
        fields = "__all__"