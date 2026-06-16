#Herança Multipla e Herança de Multinivel

#Classe Avô
class Animal:
    def __init__(self, nome):
        self.nome = nome


#Classes Pai
class Predador(Animal):
    def cacando(self):
        print(f"O animal {self.nome} está caçando! ")


class Presa(Animal):
    def fugindo(self):
        print(f"O animal {self.nome} está fugindo! ")


#Classes Filho
class Coelho(Presa):
    pass


class Tigre(Predador):
    pass


class Golfinho(Predador, Presa):
    pass



coelho1 = Coelho("Bunny")
tigre1 = Tigre("Leo")
golfinho1 = Golfinho("Billy")

coelho1.fugindo()
tigre1.cacando()
golfinho1.cacando()