# Django
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.http import JsonResponse
import config.validator as validatorMiddleware


class CompleteMiddleware(object):
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response
        print('inicio 1')


    def __call__(self, request):
        response = self.get_response(request)
        respuesta = validatorMiddleware.validator(request.path, response.data)
        respuesta = respuesta.multiplexValidator()
        print(respuesta)
        #response = self.get_response(request)
        #print (request.path)

        # Code to be executed for each request/response after
        # the view is called.
        
        if(respuesta == 'correcta'):
            pass
        else:
            return JsonResponse({'data': 'Error', 'message': 'Datos de ingreso no validos', 'status': 400 })

