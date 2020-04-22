
import modelo.validator as val

class validator():
    
    def __init__(self, path, data):
        self.response = ''
        self.path = path
        self.data = data
      #  self.multiplexValidator()
        

    def multiplexValidator(self):
        # asignar nombre de la por path
        if self.path == '/api/v1/consulta':
            respuesta = val.validatorModelo(self.data['data']['username'])
            self.response = respuesta.validateNombre()
            return self.response
        
            

