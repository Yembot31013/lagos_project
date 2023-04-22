from rest_framework import serializers
from general.models import Zone, District, School

class ZoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Zone
    fields = [
      "name"
    ]
class DistrictSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields = [
      "name"
    ]
class SchoolSerializer(serializers.ModelSerializer):
  class Meta:
    model = School
    fields = [
      "name"
    ]
