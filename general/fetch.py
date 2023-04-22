from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import School, District, Zone
from .serializer import DistrictSerializer, ZoneSerializer, SchoolSerializer


@api_view(['GET'])
def get_zone(request, *args, **kwargs):
  queryset = Zone.objects.all()
  data = ZoneSerializer(queryset, many=True).data
  return Response(data, status=200)

@api_view(['GET'])
def get_district(request, *args, **kwargs):
  local_government = request.GET.get("local_government")
  obj = Zone.objects.filter(name = local_government).first()
  if obj:
    queryset = District.objects.filter(zone = obj)
    data = DistrictSerializer(queryset, many=True).data
    return Response(data, status=200)
  return Response({}, status=500)

@api_view(['GET'])
def get_school(request, *args, **kwargs):
  local_government = request.GET.get("local_government")
  district = request.GET.get("district")
  zone_obj = Zone.objects.filter(name = local_government).first()
  district_obj = District.objects.filter(name = district, zone = zone_obj).first()
  if zone_obj and district_obj:
    print("local_government", local_government)
    print("district", district)
    print("zone_obj", zone_obj.id)
    print("district_obj", district_obj.id)
    queryset = School.objects.filter(zone = zone_obj, district = district_obj)
    print("queryset", queryset)
    data = SchoolSerializer(queryset, many=True).data
    return Response(data, status=200)
  return Response({}, status=500)