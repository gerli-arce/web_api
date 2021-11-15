from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import users as serializers
from manage_it_service.database.database import Database
from manage_it_service.database.query import Query
from uuid import uuid4
from hashlib import sha256


class setUser(APIView):
    serializer_class = serializers.setUsersSeriaizer

    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []

        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                usuario = postData.get('usuario')
                correo = postData.get('correo')
                clave = postData.get('clave')
                clave = sha256(clave.encode()).hexdigest()
                dni = postData.get('dni')
                apePater = postData.get('apePater')
                apeMater = postData.get('apeMater')
                nombres = postData.get('nombres')
                sexo = postData.get('sexo')
                fec_nac = postData.get('fec_nac')
                id_idioma = postData.get('id_idioma')

                query = Query("USUARIOS_CREATE", [
                              usuario, correo, clave, dni, apePater, apeMater, nombres, sexo, fec_nac, id_idioma], 'SET')
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)


class getActiveUsers(APIView):
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            query = Query("USUARIOS_READ_ACTIVES")
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)


class getInactiveUsers(APIView):
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            query = Query("USUARIOS_READ_INACTIVES")
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)


class searchUsers(APIView):
    serializer_class = serializers.searchUserSerializer

    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                usuario = serializer.validated_data.get('usuario')
                query = Query("USUARIOS_SEARCH", [usuario])
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)
    pass


class updateUser(APIView):
    serializer_class = serializers.updateUserSerializer

    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []

        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id = postData.get('id')
                usuario = postData.get('usuario')
                correo = postData.get('correo')
                clave = postData.get('clave')
                clave = sha256(clave.encode()).hexdigest()
                dni = postData.get('dni')
                apePater = postData.get('apePater')
                apeMater = postData.get('apeMater')
                nombres = postData.get('nombres')
                sexo = postData.get('sexo')
                fec_nac = postData.get('fec_nac')
                id_idioma = postData.get('id_idioma')
                estado = postData.get('estado')
                query = Query("USUARIOS_UPDATE", [
                              id, usuario, correo, clave, dni, apePater, apeMater, nombres, sexo, fec_nac, id_idioma, estado], 'SET')
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

    pass


class deleteUser(APIView):
    serializer_class = serializers.searchForId

    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                id_user = serializer.validated_data.get('id_user')
                query = Query("USUARIOS_DELETE_USER", [id_user], 'SET')
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)


class restoreUser(APIView):
    serializer_class = serializers.searchForId

    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                id_user = serializer.validated_data.get('id_user')
                query = Query("USUARIOS_RESTORE_USER", [id_user], 'SET')
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)


class getUsers(APIView):
    '''API PARA OBTENER LOS USUARIOS'''

    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            query = Query("USUARIOS_READ_ALL")
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)


class getUserById(APIView):
    """API PARA OBTENER USUARIO X USERNAME."""
    serializer_class = serializers.searchForId

    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                id_user = serializer.validated_data.get('id_user')
                query = Query("USUARIOS_READ_ONE", [id_user])
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getOne()
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)


class validateUser(APIView):
    '''OBTENER USUARIO SEGÚN USUARIO Y CONTRASEÑA'''
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        statusCode = 200
        message = 'NTS'
        data = dict()
        session = dict()
        db = Database()
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                username = postData.get('username')
                password = postData.get('password')
                password = sha256(password.encode()).hexdigest()
                cursor = db.connect()
                query = "USUARIOS_READ_USERNAME_PASSWORD ?, ?"
                parameters = (username, password)
                cursor.execute(query, parameters)
                columns = [i[0] for i in cursor.description]
                row = cursor.fetchall()
                if (len(row) == 0):
                    statusCode = 400
                    message = 'Usuario y/o contraseña incorrectos'
                else:
                    i = 0
                    for x in row[0]:
                        data[columns[i]] = x
                        i = i + 1
                    if data['estado'] == False:
                        statusCode = 400
                        message = 'Este usuario esta inactivo'
                    else:
                        statusCode = 200
                        message = 'Operación correcta'
                        session['uuid'] = uuid4()
                        session['rol'] = 'USER'
            else:
                statusCode = 400
                message = 'Error en la petición'
        except Exception as e:
            statusCode = 400
            message = 'Error: ' + e
        finally:
            db.disconnect()
            res = {
                'status': statusCode,
                'message': message,
                'data': data,
                'session': session
            }
            if (statusCode == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)
