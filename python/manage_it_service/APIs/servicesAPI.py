from typing import final
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import services as serializers
from manage_it_service.database.query import Query
from uuid import uuid4
from hashlib import sha256

class setService(APIView):
    serializer_class = serializers.setService
    def post(self, request):
        res = {}
        data = []
        session = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = data
        res['session'] = session
        try:
            serial = self.serializer_class(data = request.data)
            if serial.is_valid():
                service = serial.validated_data.get('service')
                query = Query('SERVICIOS_CREATE', [service], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'El servicio se agregó correctamente'
                else:
                    res['message'] = query.message
            else:
                res['message'] = 'Falló en la petición'
        except Exception as e:
            res['message'] = 'Error: ' + e
        finally:
            print(res)
            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getServices(APIView):
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            query = Query('SERVICIOS_READ_ALL')
            if query.status:
                res['status'] = 200
                res['message'] = 'Operación correcta'
                res['data'] = query.getAll()
            else:
                res['message'] = query.message
        except Exception as e:
            res['message'] = 'Error: ' + e
        finally:
            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)