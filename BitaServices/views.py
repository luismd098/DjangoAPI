from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BitaServices.models import Usuario,Reporte,Bitacora,RelBitacoraLicencia

# from BitaServices.serializers import UsersSerializer

from  BitaServices.utilities.cifrado import AESCipher

# Create your views here.

@csrf_exempt
def loginApi(request,id=0):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        txt = data['txt']
        type = data['type']
        cipher = AESCipher()
        if type == 1:
            psw = cipher.encrypt(txt)
        elif type == 2:
            psw = cipher.decrypt(txt)
        return JsonResponse({'msg':str(psw)},safe=False)
        
        
        
        

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