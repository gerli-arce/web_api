from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Serializar una campo para probar nuestro APIView'''
    name = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=100)
    gmail = serializers.CharField(max_length=100)
    edad = serializers.CharField(max_length=100)


# Serializador de SERVICES
class setService(serializers.Serializer):
    service = serializers.CharField(max_length = 45)