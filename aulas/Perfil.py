class Perfil(object):
   'Classe padrão para perfis de usuários'
   def __init__(self, nome, telefone, empresa):
      if (len(nome) < 3):
         raise ValueError('Nome deve ter pelo menos 3 caracteres')
      self.nome = nome
      self.telefone = telefone
      self.empresa = empresa
      self.__curtidas = 0

   def imprimir(self):
      saida = "nome: " + self.nome + " - Telefone: " + self.telefone
      print(saida)

   def curtir(self):
      self.__curtidas += 1

   def obter_curtidas(self):
      return self.__curtidas

   @classmethod
   def gerar_perfis(classe, nome_arquivo):
      arquivo = open(nome_arquivo, 'r')
      perfis = []
      for linha in arquivo:
         valores = linha.split(',')
         perfis.append(classe(*valores))
      arquivo.close()
      return perfis

class PerfilVip(Perfil):

   def __init__(self, nome, telefone, empresa, apelido=''):
      super().__init__(nome,telefone,empresa)
      self.apelido = apelido

   def obter_creditos(self):
      return super().obter_curtidas() * 10