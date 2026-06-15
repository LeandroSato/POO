class Casa:
    def __init__(self, cor, quartos, banheiros): #Constructor
        self.cor = cor #associar o constructor ao atributo
        self.quartos = quartos
        self.banheiros = banheiros
    
    def mostrar_cor(self): #Método
        print(f"A cor da casa é {self.cor}")

    def mostrar_quartos(self):
        print(f"Esta casa tem {self.quartos} quartos")

    def mostrar_banheiros(self):
        print(f"Esta casa tem {self.banheiros} banheiros")

    def adicionar_quarto(self):
        self.quartos += 1
        print(f"Esta casa tem {self.quartos} quartos")

    def trocar_cor(self, nova_cor):
        print(f"Pintando a casa de {self.cor} para {nova_cor}")
    
casa1 = Casa('Azul', 4, 3)
casa2 = Casa("Amarelo", 6, 4)

print("\nCasa 1: ") #\n pula linha
casa1.mostrar_cor() #Instancias
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.trocar_cor("Vermelho")

print("\nCasa 2: ")
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()