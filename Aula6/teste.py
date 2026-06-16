class Familia:
  def __init__ (self, funcao):
    self.funcao = funcao

class Pai(Familia):
  def dever(self):
    print(f"O pai {self.funcao}! ")


class Mae(Familia):
  def dever(self):
    print(f"A mãe {self.funcao}! ")
  

class Filhos(Familia):
  def dever(self):
    print(f"Os filhos {self.funcao}! ")


pai1 = Pai("trabalha")
mae1 = Mae("faz a comida")
filhos1 = Filhos("estudam")

pai1.dever()
mae1.dever()
filhos1.dever()