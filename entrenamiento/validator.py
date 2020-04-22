
class validatorModelo():

    def __init__(self):
        self.schema = ''
        #self.validacion = self.validateNombre(nombre)

    def validateNombre (self, schema):
        self.schema = schema
        print(schema)
        if self.schema['username'] == 'Danni':
            return True
        else:
            return False