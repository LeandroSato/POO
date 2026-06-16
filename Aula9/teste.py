#Agregation: quando o objeto(carro) é criado por outros objetos(motores).
#Esses outros objetos não precisam existir sem o objeto principal

class Livro:
    def __init__(self, nome, qntP, disponivel):
        self.nome = nome
        self.qntP = qntP
        self.disponivel = disponivel 

class Autor:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro) #append: adicionar um item a uma lista

    def listar_livros(self):
        for livro in self.livros:
            print(f"O livro "{livro.nome}" tem {livro.qntP} e está {"Disponível" if livro.disponivel else "Indispoível"}")
            


#CRIANDO OS LIVROS (objetos)
livro1 = Livro("O mago" , 250, True)
livro2 = Livro("Judgment", 457, False)

#CRIAR O AUTOR E ADICIONAR O LIVRO A ELE
autor = Autor()
autor.adicionar_livro(livro1)


#LISTAR 
autor.listar_livros()
