from django.shortcuts import render
# from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from BitaServices.models import Usuario,Reporte,Bitacora,RelBitacoraLicencia

from BitaServices.serializers import UsuarioSerializer

from  BitaServices.utilities.cifrado import AESCipher

# Create your views here.

@csrf_exempt
def loginApi(request,id=0):
    # try: 
        if request.method == 'POST':
            data = JSONParser().parse(request)
            cipher = AESCipher()
            
            user = data['user']
            password = data['password']
            
            user = user.lower()
            
            if not Usuario.objects.filter(Usuario = user).exists():
                return JsonResponse({'Msg':'El usuario no existe, favor de validar.','Status':1},safe=False)
            
            user_data = Usuario.objects.get(Usuario = user)
            
            if user_data.Activo == False:
                return JsonResponse({'Msg':'El usuario se encuentra dado de baja.','Status':1},safe=False)
                        
            if not cipher.validate(password,user_data.Password):
                return JsonResponse({'Msg':'La contraseña ingresada es incorrecta, favor de validar.','Status':1},safe=False)
                
            user_serializer = UsuarioSerializer(user_data)
            json_data = user_serializer.data     
            json_data['Status'] = 0                 
            json_data['Msg'] = ''                 
            
            return JsonResponse(json_data,safe=False)                
    # except:
        # return JsonResponse({'Msg':'Algo salio mal, por favor comunicate con el administrador.','Status':1},safe=False)
        
        
def convertToJson(data):
   data_dict = ValuesQuerySetToDict(data)
   response = json.dumps(data_dict)
   return response

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]        
        
        

# @csrf_exempt
# def userApi(request,id=0):
#     if request.method == 'GET':
#         users = Users.objects.all()
#         users_serializer = UsersSerializer(users, many = True)
#         return JsonResponse(users_serializer.data,safe=False)
#     elif request.method == 'POST':
#         users_data = JSONParser().parse(request)
#         users_serializer = UsersSerializer(data=users_data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return JsonResponse("Correcto!",safe=False)
#         return JsonResponse('Algo salio mal al agregar',safe=False)
#     elif request.method == 'PUT':
#         user_data = JSONParser().parse(request)
#         user = Users.objects.get(UserId = user_data['UserId'])
#         users_serializer = UsersSerializer(user,data = user_data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return JsonResponse("Update Correcto!",safe=False)
#         return JsonResponse('Algo salio mal al actualizar',safe=False)
#     elif request.method == 'DELETE':
#         if Users.objects.filter(UserId = id).exists():
#             user = Users.objects.get(UserId = id)
#             user.delete()
#             return JsonResponse(['msg','Usuario eliminado exitosamente'],safe=False)
        
#         return JsonResponse({'msg':'El usuario no existe','status':1},safe=False)