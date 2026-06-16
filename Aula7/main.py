#Sistema de Escola

class Escola:
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status

    def apresentar(self):
        print(f"Meu nome é {self.nome}")

    def verificar_status(self):
        print(f"Status: {"ATIVO" if self.status else "INATIVO"}")#if e else de forma compacta


class Aluno(Escola):
    def __init__(self, nome, idade, status, ano):
        super().__init__(nome, idade, status)
        self.ano = ano

    def apresentar(self): #A classe filho sempre se sobrepõe a do pai
        super().apresentar()# Para mostrar a do pai usar o super
        print(f"Tenho {self.idade} anos de idade e estou no {self.ano} ano da escola! ")

class Professor(Escola):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia

    def apresentar(self): 
        super().apresentar()
        print(f"Sou professor da escola e tenho {self.idade} anos de idade. Dou matéria de {self.materia}! ")

class Assistente(Escola):
    def __init__(self, nome, idade, status, bloco):
        super().__init__(nome, idade, status)
        self.bloco = bloco

    def apresentar(self): 
        super().apresentar()
        print(f"Sou assistente da escola e tenho {self.idade} anos de idade. Sou do {self.bloco}! ")


#ALUNO
print("-----ALUNO-----")
a1 = Aluno(nome="Marcos", idade=12, status=True, ano=8) #DECLARAR PARA FICAR MAIS VISIVEL E ORGANIZADO(nome, idade...)
a1.apresentar()
a1.verificar_status()
print("\n")

#PROFESSOR
print("-----PROFESSOR-----")
p1 = Professor(nome="João", idade=37, status=True, materia="Matemática")
p1.apresentar()
p1.verificar_status()
print("\n")

#ASSISTENTE
print("-----ASSISTENTE-----")
ass1 = Assistente(nome="Maria", idade=25, status=False, bloco="Bloco C")
ass1.apresentar()
ass1.verificar_status()
print("\n")
