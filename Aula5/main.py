class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, o meu nome é {self.nome} e tenho {self.idade} anos de idade. ")

    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade) #Puxa as informações da classe pai(Pessoa)
        self.cargo = cargo

    def trabalhar(self):
        print(f"{self.nome} está atuando como {self.cargo}! ")


class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo

    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f"Ola {self.nome}, sua compra de R${valor_compra:.2f} foi aprovada! Seu saldo atual é de R${self.saldo:.2f}! ")
        else:
            print("Saldo Insuficiente! ")


#FUNCIONARIO
print("\n Funcionários")
f1 = Funcionario("Maria", 38, "Gerente de contas")
f1.apresentar()
f1.trabalhar()

#CLIENTE
print("\n _____________________________")
print("\n Clientes")
c1 = Cliente("Arthur", 16, 200)
c2 = Cliente("José", 31, 50)
c1.apresentar()
c1.comprar(300)

print("\n _____________________________")
print("\n")
c2.apresentar()
c2.comprar(100)