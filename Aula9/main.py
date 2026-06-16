#Agregation: quando o objeto(carro) é criado por outros objetos(motores).
#Esses outros objetos não precisam existir sem o objeto principal

class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []

    def adicionar_motor(self, motor):
        self.motores.append(motor) #append: adicionar um item a uma lista

    def listar_motores(self):
        for motor in self.motores:
            print(f"Marca: {motor.marca} - {motor.potencia} cavalos de potencia ")


#CRIANDO OS MOTORES (objetos)
motor_v6 = Motor("Ford", 300)
motor_v8 = Motor("Ferrari", 650)
motor_v12 = Motor("Lamborghini", 950)

#CRIAR O CARRO E ADICIONAR O MOTOR A ELE
carro = Carro()
carro.adicionar_motor(motor_v6)
carro.adicionar_motor(motor_v8)
carro.adicionar_motor(motor_v12)

#LISTAR OS MOTORES
carro.listar_motores() 
