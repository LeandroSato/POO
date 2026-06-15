class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f"Eu sou o(a) {self.especie} chamado(a) {self.nome} ")

class Gato(Animal):

    def som(self):
        print("Miau")

    def acao(self):
        print("O gato está arranhando")

class Cachorro(Animal):
    
    def som(self):
        print("Au Au")

    def acao(self):
        print("O cachorro está abanando o rabo")    


class Elefante(Animal):
    
    def som(self):
        print("Pruuuuuuu")

    def acao(self):
        print("O elefante bebe água com a tromba") 

print("\n Gato")
gato1 = Gato("Felix", "Branco", "Siamês")
gato1.apresentar()
gato1.som()
gato1.acao()

print("\n Cachorro")
cachorro1 = Cachorro("Russo", "Preto", "Pastor Alemão")
cachorro2 = Cachorro("Bella", "Branca", "Maltez")
cachorro1.apresentar()
cachorro1.som()
cachorro1.acao()
cachorro2.apresentar()

print("\n Elefante")
elefante1 = Elefante("Fred", "Marrom", "Asiático")
elefante1.apresentar()
elefante1.som()
elefante1.acao()