#Nestled

#Criar a classe Main

class Computador:
    def __init__(self, modelo, gpu_nome, gpu_memoria,
                 cpu_nome, cpu_cores, cpu_clock, 
                 memoria_modelo, memoria_GgbAM):
        
        self.modelo = modelo
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(cpu_nome, cpu_cores, cpu_clock)
        self.memoria = self.Memoria(memoria_modelo, memoria_GgbAM )

    def mostrar_configuração(self):
        print(f"Computador: {self.modelo}")
        self.gpu.mostrar_gpu() #linkar
        self.cpu.mostrar_cpu()
        self.memoria.mostrar_memoria()

    class GPU: #Nested Class
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb

        def mostrar_gpu(self):
            print(f"GPU: {self.nome} - {self.memoria_gb} ")

    class CPU:
        def __init__(self, nome, cores, clock_gh):
            self.nome = nome
            self.cores = cores
            self.clock_gh = clock_gh

        def mostrar_cpu(self):
            print(f"CPU: {self.nome} - {self.cores} núcleos - {self.clock_gh}GHz ")

    class Memoria:
        def __init__(self, modelo, gbRAM):
            self.modelo = modelo
            self.gbRAM = gbRAM 

        def mostrar_memoria(self):
            print(f"Memória: {self.modelo} - {self.gbRAM}gbRAM ")

#Utilização

pc1 = Computador(modelo="Dell XPS", gpu_nome="NVIDIA RTX 4090", gpu_memoria=24,
                 cpu_nome="Intel Core i7", cpu_cores=8, cpu_clock=4.6,
                 memoria_modelo="Kignston", memoria_GgbAM=16
                 )

pc1.mostrar_configuração()
