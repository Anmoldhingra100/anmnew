from rest_framework import serializers
from solar_app.models import MySolarrr

class EnergyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySolarrr
        fields = '__all__'
