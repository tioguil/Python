

class Usuario(object):

    def __init__(self, idUsuario ="", email="", senha="", fk_idcliente=""):
        self.idUsuario = idUsuario
        self.email = email
        self.senha = senha
        self.fk_idcliente = fk_idcliente


    def imprimir(self):
        print('email: ', self.email)