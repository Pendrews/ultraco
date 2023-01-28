from django.contrib.auth.models import User
from . models import Profile
import requests


def get_ultra_user():
    url='http://192.168.100.54:8888/ords/BPT/testuser/usertest'
    res = requests.get(url)
    data = res.json()['items']
    for data in data:
        if User.objects.filter(username=data['accountno']).exists():
            User.objects.filter(username=data['accountno']).update(last_name=data['surname'], first_name=data['first_name'], email=data['email'])
            print ('updated')
        else:
            User.objects.create(username=data['accountno'],last_name=data['surname'], first_name=data['first_name'], email=data['email'])
            print('Created')


def get_ultra_profile():
    url='http://192.168.100.54:8888/ords/BPT/userprofile/profile'
    res = requests.get(url)
    data = res.json()['items']
    for data in data:
        if Profile.objects.filter(user=data['ultra_conetid']).exists():
            Profile.objects.filter(user=data['ultra_conetid']).update(dob=data['dob'],age=data['age'],gender=data['gender'],
                                                                      country=data['nationality'], country_of_birth=data['country_of_birth'],
                                                                      place_of_birth=data['place_of_birth'], phone = data['phone'], alt_phone=data['alternative_phone'],
                                                                      dig_address =data['digital_address'],postal_address=data['postal_address'], res_address=data['residential_address'],
                                                                      ssnit=data['ssnit'], national_id=data['id_no'],nok=data['next_of_kin'],nok_address=data['nok_address'],nok_rel=data['nok_relationship'],
                                                                      nok_phone=data['next_of_kin_tel'], father_name=data['name_of_father'],father_address=data['fathers_address'], mother_name=data['name_of_mother'],mother_address=data['mothers_address'])
            print('updated')
        else:
            print('no existing user found')




    # for data in data:
    #     if User.objects.filter(username=data['accountno']).exists():
    #         User.objects.filter(username=data['accountno']).update(last_name=data['surname'], first_name=data['first_name'])
    #         # User.objects.update(last_name=data['surname'], first_name=data['first_name'])