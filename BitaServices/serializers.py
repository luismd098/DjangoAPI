from rest_framework import serializers
from BitaServices.models import Usuario,Privilegio


class PrivilegioSerializer(serializers.ModelSerializer):
    class Meta:
            model = Privilegio
            fields = '__all__'
            
class UsuarioSerializer(serializers.ModelSerializer):
    Privilegios = PrivilegioSerializer(read_only=True)
    class Meta:
            model = Usuario
            fields = ('UsuarioId','Usuario','Password','Nombre','Apellidos','Activo','Privilegios')
    
    