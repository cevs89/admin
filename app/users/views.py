from django.http import JsonResponse
from django.contrib.auth.models import User
from users.models import UserProfile
from users.serializers import ValidateUsersRegister
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
import json


@api_view(['POST'])
@parser_classes((JSONParser,))
@permission_classes((AllowAny,))
def RegisterUser(request):
    data = json.loads(request.body.decode("utf-8"))
    validate_fields = ValidateUsersRegister(data=data)
    if validate_fields.is_valid():
        valid_data = validate_fields.validated_data
        username = valid_data['username']
        email = valid_data['email']
        password = valid_data['password']
        first_name = valid_data['first_name']
        last_name = valid_data['last_name']
        # Profile
        academic_level = valid_data['academic_level']
        address = valid_data['address']
        city = valid_data['city']
        country = valid_data['country']

        if User.objects.filter(username=username).exists():
            return JsonResponse({'Error': 'User already exists'})
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            profile = UserProfile(
                user=user, academic_level=academic_level,
                address=address, city=city, country=country
                )
            profile.save()
            Token.objects.create(user=user)
            return JsonResponse({'success': True, 'msg': 'User has been created'})
    else:
        return JsonResponse(validate_fields.errors)


@api_view(['POST'])
@parser_classes((JSONParser,))
@permission_classes((permissions.IsAuthenticated,))
def GetProfile(request):
    data = json.loads(request.body.decode("utf-8"))
    id_user = data['id_user']
    try:
        profile = UserProfile.objects.get(user_id=id_user)
    except UserProfile.DoesNotExist:
        return JsonResponse({'token': 'User not exist'})

    return JsonResponse({
        'username': profile.user.username, 'academic_level': profile.academic_level,
        'country': profile.country, 'address': profile.address,
        'city': profile.city
        })
