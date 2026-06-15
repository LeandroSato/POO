# Aula 1

## Programação Orientada a Objetos (POO)

Nesta aula, aprendemos os conceitos básicos de POO usando uma classe que representa uma casa.

### Conceitos abordados

- **Classe**: define a estrutura de um objeto. No exemplo, a classe `Casa` representa a planta de uma casa.
- **Construtor**: método especial `__init__` usado para criar objetos com atributos iniciais.
- **Atributos**: propriedades do objeto, como `cor`, `quartos` e `banheiros`.
- **Métodos**: funções dentro da classe que realizam ações sobre os objetos.

### Classe `Casa`

A classe `Casa` possui:

- `__init__(self, cor, quartos, banheiros)`: inicializa uma casa com cor, número de quartos e número de banheiros.
- `mostrar_cor(self)`: exibe a cor da casa.
- `mostrar_quartos(self)`: exibe o número de quartos.
- `mostrar_banheiros(self)`: exibe o número de banheiros.
- `adicionar_quarto(self)`: aumenta em 1 o número de quartos.
- `trocar_cor(self, nova_cor)`: simula a troca da cor da casa.

### Exemplo de uso

No arquivo `Aula1/main.py`, são criadas duas casas e chamados métodos para mostrar seus atributos e alterar alguns valores.

Exemplo de execução:

```python
casa1 = Casa('Azul', 4, 3)
casa2 = Casa('Amarelo', 6, 4)

print("\nCasa 1:")
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.trocar_cor("Vermelho")

print("\nCasa 2:")
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()
```

### Aprendizado

- Como definir uma classe em Python
- Como usar o construtor para inicializar atributos
- Como criar métodos para manipular e exibir dados dos objetos
- Como instanciar objetos e invocar métodos