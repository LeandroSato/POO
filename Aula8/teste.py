class Cachorro:
    def acao(self):
        print("AU AU AU")

class Gato:
    def acao(self):
        print("MIAU")


animais = {Cachorro(), Gato()}

for a in animais:
    a.acao()
