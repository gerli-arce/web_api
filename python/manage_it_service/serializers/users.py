from rest_framework import serializers

class searchForId(serializers.Serializer):
    # buscar usuario por id
    id_user = serializers.CharField(max_length = 8)

class setUsersSeriaizer(serializers.Serializer):
    # Agregar nuebo usuario
    usuario = serializers.CharField(max_length = 16)
    correo = serializers.CharField(max_length = 320)
    clave = serializers.CharField(max_length = 64)
    dni = serializers.CharField(max_length = 8)
    apePater = serializers.CharField(max_length = 15)
    apeMater = serializers.CharField(max_length = 15)
    nombres = serializers.CharField(max_length = 45)
    sexo = serializers.CharField(max_length = 1)
    fec_nac = serializers.CharField(max_length = 10)
    id_idioma = serializers.CharField(max_length = 8)

class searchUserSerializer(serializers.Serializer):
    # buscar un usuario
    usuario = serializers.CharField(max_length = 50)

class updateUserSerializer(serializers.Serializer):
    # Agregar nuebo usuario
    id = serializers.CharField(max_length = 8)
    usuario = serializers.CharField(max_length = 16)
    correo = serializers.EmailField(max_length = 320)
    clave = serializers.CharField(max_length = 64)
    dni = serializers.CharField(max_length = 8)
    apePater = serializers.CharField(max_length = 15)
    apeMater = serializers.CharField(max_length = 15)
    nombres = serializers.CharField(max_length = 45)
    sexo = serializers.CharField(max_length = 1)
    fec_nac = serializers.DateField(format = '%Y-%m-%d', input_formats=None)
    id_idioma = serializers.CharField(max_length = 8)
    estado = serializers.ChoiceField(choices = (('1', 'ACTIVO'), ('0', 'INACTIVO')))

class LoginSerializer(serializers.Serializer):
    '''Datos que vienen del login'''
    username = serializers.CharField(max_length = 320)
    password = serializers.CharField(max_length = 64)
