from django.contrib.auth.models import *
from rest_framework import serializers
from .models import *

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id','Descripcion', 'Frecuencia', 'Probabilidad', 'TipoEvento']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only':True, 'required': True}}

    def create(self, validate_data): #validate_data es para hacer hash en la contraseña
        user = User.objects.create_user(**validate_data)
        return user