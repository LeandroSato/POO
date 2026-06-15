class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Cargo: {self.cargo}")

    def promover(self, novo_cargo):
        print(f"{self.nome} foi promovido(a) para a nova função de {novo_cargo}! ") 

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f"Atualizando a idade de {self.idade} para {nova_idade}")    
        else:
            print("A nova idade tem que ser maior que a anteiror")   
    
colaborador1 = Pessoa("Leandro", 19, "Assistente Junior")
colaborador2 = Pessoa("Anna", 26, "Dev Junior")

colaborador2.informacoes()
colaborador2.promover("Assistente Pleno")
colaborador2.atualizar_idade(27)