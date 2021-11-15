from rest_framework import serializers

class setCurrencySerializer(serializers.Serializer):
    # Agregar nuebo currency
    moneda = serializers.CharField(max_length = 12)
    estado = serializers.ChoiceField(choices = (('1', 'ACTIVO'), ('0', 'INACTIVO')))

class searchCurrencySerializer(serializers.Serializer):
    # Buscar moneda
    currency = serializers.CharField(max_length = 50)

class updateCurrencySerializer(serializers.Serializer):
    # Actualizar currency
    id = serializers.CharField(max_length = 8)
    moneda = serializers.CharField(max_length = 12)
    estado = serializers.ChoiceField(choices = (('1', 'ACTIVO'), ('0', 'INACTIVO')))

class searchForId(serializers.Serializer):
    #buscar por id
    id = serializers.CharField(max_length = 8)
