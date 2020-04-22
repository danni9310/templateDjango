from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

import entrenamiento.validator as validatorMiddleware
# Create your views here.

validador = validatorMiddleware.validatorModelo()

@api_view(["POST"])
def consulta(request):
    if (validador.validateNombre(request.data)):
        return Response({'data': request.data, 'message': 'Post realizado', 'status': 400 },
                        status=HTTP_200_OK)
    else: 
        return Response({'data': request.data, 'message': 'Datos de ingreso invalidos', 'status': 400 },
                status=HTTP_404_NOT_FOUND)


@api_view(["GET"])
def respuesta(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

