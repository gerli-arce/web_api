from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from web.database.query import Query
from manage_it_service.serializers import currency as serializers

class setCurrency(APIView):
    serializer_class = serializers.setCurrencySerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                moneda = postData.get('moneda')
                estado = postData.get('estado')
              

                query = Query("MONEDAS_CREATE",[moneda, estado], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)
        pass

class getCurrencyes(APIView):
    
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            query = Query("MONEDAS_READ_ALL")
            if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
            else:
                res['message'] = query.message
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getActiveCurrencies(APIView):
    
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            query = Query("MONEDAS_READ_ACTIVES")
            if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
            else:
                res['message'] = query.message
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getInactiveCurrencies(APIView):
    
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            query = Query("MONEDAS_READ_INACTIVES")
            if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
            else:
                res['message'] = query.message
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class searchCurrency(APIView):
    serializer_class = serializers.searchCurrencySerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                currency = serializer.validated_data.get('currency')
                query = Query("MONEDAS_SEARCH",[currency])
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class updateCurrency(APIView):
    serializer_class = serializers.updateCurrencySerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id = postData.get('id')
                moneda = postData.get('moneda')
                estado = postData.get('estado')
              

                query = Query("MONEDA_UPDATE",[id,moneda, estado], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class deleteCurrency(APIView):
    serializer_class = serializers.searchForId
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("MONEDA_DELETE",[id], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class restoreCurrency(APIView):
    serializer_class = serializers.searchForId
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("MONEDA_RESTORE",[id], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)
