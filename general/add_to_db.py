import pandas as pd
from pathlib import Path
import os
from .models import School, Zone, District



def import_data(request):
    BASE_DIR = Path(__file__).resolve().parent

    file_name = os.path.join(BASE_DIR, 'doc.xlsx')
    print(file_name)
    df = pd.read_excel(file_name, sheet_name='Sheet1')

    # Create a dictionary of district objects for faster lookups
    district_objects = {district.name: district for district in District.objects.all()}

    # Create a dictionary of zone objects for faster lookups
    zone_objects = {zone.name: zone.district.name for zone in Zone.objects.all()}

    for index, row in df.iterrows():
        district = district_objects.get(row['DISTRICT'])
        if not district:
            # District not found, create a new one
            district = District.objects.create(name=row['DISTRICT'])
            district_objects[row['DISTRICT']] = district

        zone = zone_objects.get(row['ZONE'])
        if not zone or zone != row['DISTRICT']:
            # Zone not found, create a new one and link it to the district
            zone = Zone.objects.create(name=row['ZONE'], district=district)
            zone_objects[row['ZONE']] = row['DISTRICT']
        else:
            zone = Zone.objects.get(name=row['ZONE'], district=district)


        # Create a new school object and link it to the district and zone
        school = School.objects.create(
            name=row['NAME OF SCHOOL'],
            zone=zone,
            district=district,
            school_level=row['CATEGORY'],
        )

        print(f"{index} => {row['ZONE']} | {row['DISTRICT']} | {row['CATEGORY']} | {row['NAME OF SCHOOL']} ")        
    context = {
            "title": "Warning!!!",
            "description": "Sorry You can't access this page",
            "icon": ""
        }
    return render(request, 'general/verify.html', context)

def import_datas(request):
    BASE_DIR = Path(__file__).resolve().parent

    file_name = os.path.join(BASE_DIR, 'doc.xlsx')
    print(file_name)
    df = pd.read_excel(file_name, sheet_name='Sheet1')

    # Create a dictionary of zone objects for faster lookups
    zone_objects = {zone.name: zone for zone in Zone.objects.all()}

    # Create a dictionary of district objects for faster lookups
    district_objects = {district.name: district for district in District.objects.all()}

    for index, row in df.iterrows():
        zone = zone_objects.get(row['ZONE'])
        if not zone:
            # Zone not found, create a new one
            zone = Zone.objects.create(name=row['ZONE'])
            zone_objects[row['ZONE']] = zone

        district = district_objects.get(row['DISTRICT'])
        if not district:
            # District not found, create a new one and link it to the zone
            district = District.objects.create(name=row['DISTRICT'], zone=zone)
            district_objects[row['DISTRICT']] = district

        # Create a new school object and link it to the district and zone
        school = School.objects.create(
            name=row['NAME OF SCHOOL'],
            zone=zone,
            district=district,
            school_level=row['CATEGORY'],
        )

        print(f"{index} => {row['ZONE']} | {row['DISTRICT']} | {row['CATEGORY']} | {row['NAME OF SCHOOL']} ")

    context = {
            "title": "Warning!!!",
            "description": "Sorry You can't access this page",
            "icon": ""
        }
    return render(request, 'general/verify.html', context)
