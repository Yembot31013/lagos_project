from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import School, District, Zone
from .serializer import DistrictSerializer, ZoneSerializer, SchoolSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
def get_district(request, *args, **kwargs):
    queryset = District.objects.all()
    data = DistrictSerializer(queryset, many=True).data
    return Response(data, status=200)

@api_view(['GET'])
def get_zone(request, *args, **kwargs):
  district = request.GET.get("district")
  obj = District.objects.filter(name = district).first()
  if obj:
    queryset = Zone.objects.filter(district_id = obj.id)
    data = ZoneSerializer(queryset, many=True).data
    return Response(data, status=200)
  return Response({}, status=500)

@api_view(['GET'])
def get_school(request, *args, **kwargs):
  local_government = request.GET.get("local_government")
  district = request.GET.get("district")
  district_obj = District.objects.filter(name = district).first()
  zone_obj = Zone.objects.filter(name = local_government, district = district_obj).first()
  if zone_obj and district_obj:
    queryset = School.objects.filter(zone = zone_obj, district = district_obj)
    data = SchoolSerializer(queryset, many=True).data
    return Response(data, status=200)
  return Response({}, status=500)

@api_view(['GET'])
def check_email_user(request, *args, **kwargs):
  username = request.GET.get("username")
  email = request.GET.get("email")
  userName = User.objects.filter(username=username)
  email = User.objects.filter(email=email)
  if email:
    return Response({}, status=400)
  elif userName:
    return Response({}, status=400)
  return Response({}, status=200)