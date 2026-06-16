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

# Aula 2

## Programação Orientada a Objetos (POO)

Nesta aula, a implementação aborda um objeto `carro` e o controle do seu estado.

### Conceitos abordados

- **Classe**: modelo para representar um carro.
- **Atributos**: `cor`, `ano`, `ligado` e `seta`.
- **Métodos**: ações como ligar, desligar e ativar a seta.
- **Estado do objeto**: o carro só pode ligar a seta quando estiver ligado.

### Classe `carro`

A classe `carro` possui:

- `__init__(self, cor, ano)`: inicializa cor, ano, ligado e seta.
- `informacoes(self)`: exibe cor e ano do carro.
- `ligar(self)`: liga o carro quando estiver desligado.
- `desligar(self)`: desliga o carro quando estiver ligado.
- `ligar_seta(self, direcao)`: ativa a seta apenas com o carro ligado.

### Exemplo de uso

No arquivo `Aula2/main.py`, o carro é criado e são chamados métodos para exibir informações, desligar o carro e ligar a seta.

Exemplo de execução:

```python
carro1 = carro("Preto", 2021)
carro1.informacoes()
carro1.desligar()
carro1.ligar_seta("direita")
```

### Aprendizado

- Como trabalhar com estados booleanos em objetos
- Como validar condições antes de executar ações
- Como interagir com métodos que mudam o estado do objeto

# Aula 3

## Programação Orientada a Objetos (POO)

Nesta aula, aprendemos a modelar uma pessoa com atributos e ações relacionadas a promoção e atualização de idade.

### Conceitos abordados

- **Classe**: representa uma pessoa com nome, idade e cargo.
- **Atributos**: `nome`, `idade` e `cargo`.
- **Métodos**: ações para exibir informações, promover e atualizar idade.
- **Validação**: a idade só é atualizada se for maior que a idade atual.

### Classe `Pessoa`

A classe `Pessoa` possui:

- `__init__(self, nome, idade, cargo)`: inicializa os atributos da pessoa.
- `informacoes(self)`: exibe nome, idade e cargo.
- `promover(self, novo_cargo)`: mostra uma mensagem de promoção.
- `atualizar_idade(self, nova_idade)`: atualiza a idade somente se `nova_idade` for maior que a idade atual.

### Exemplo de uso

No arquivo `Aula3/main.py`, são criadas duas pessoas e chamados métodos para exibir informações, promover uma pessoa e atualizar a sua idade.

Exemplo de execução:

```python
colaborador1 = Pessoa("Leandro", 19, "Assistente Junior")
colaborador2 = Pessoa("Anna", 26, "Dev Junior")

colaborador2.informacoes()
colaborador2.promover("Assistente Pleno")
colaborador2.atualizar_idade(27)
```

### Aprendizado

- Como criar uma classe com atributos e métodos em Python
- Como aplicar validação dentro de métodos
- Como representar mudanças de estado em objetos
- Como usar métodos para exibir e modificar dados do objeto

# Aula 4

## Herança em POO

Nesta aula, exploramos herança e polimorfismo usando uma hierarquia de animais.

### Conceitos abordados

- **Herança**: como subclasses (`Gato`, `Cachorro`, `Elefante`) herdam atributos e métodos de uma classe base (`Animal`).
- **Polimorfismo**: métodos com o mesmo nome (`som`, `acao`) possuem implementações diferentes nas subclasses.
- **Reuso de código**: a classe base `Animal` contém atributos e métodos comuns reutilizados pelas subclasses.
- **Especialização**: cada subclasse implementa comportamentos específicos (por exemplo, `Miau`, `Au Au`).

### Classe `Animal` e subclasses

- `Animal(nome, cor, especie)`: classe base com método `apresentar()`.
- `Gato`, `Cachorro`, `Elefante`: subclasses que implementam `som()` e `acao()`.

### Exemplo de uso

No arquivo `Aula4/main.py`, são instanciados um `Gato`, dois `Cachorro` e um `Elefante`, e demonstrados seus métodos:

```python
gato1 = Gato("Felix", "Branco", "Siamês")
gato1.apresentar()
gato1.som()
gato1.acao()

cachorro1 = Cachorro("Russo", "Preto", "Pastor Alemão")
cachorro1.apresentar()
cachorro1.som()
cachorro1.acao()

cachorro2 = Cachorro("Bella", "Branca", "Maltez")
cachorro2.apresentar()

elefante1 = Elefante("Fred", "Marrom", "Asiático")
elefante1.apresentar()
elefante1.som()
elefante1.acao()
```

### Aprendizado

- Como criar uma hierarquia de classes com herança
- Como sobrescrever métodos nas subclasses
- Como usar polimorfismo para tratar objetos de forma genérica
- Como organizar código reaproveitando a classe base

# Aula 5

## Herança com `super()` e Especialização

Nesta aula, exploramos herança mais profunda usando `super()` e criamos múltiplas subclasses especializadas a partir de uma classe base.

### Conceitos abordados

- **Herança**: classes `Funcionario` e `Cliente` herdam da classe base `Pessoa`.
- **super()**: usado para chamar o construtor da classe pai e reutilizar seu código.

# Aula 6

## Herança múltipla e herança de multinível

Nesta aula, aprendemos a combinar herança de multinível e herança múltipla usando uma hierarquia de animais.

### Conceitos abordados

- **Herança de multinível**: `Coelho` herda de `Presa`, que herda de `Animal`.
- **Herança múltipla**: `Golfinho` herda de `Predador` e `Presa`.
- **Métodos herdados**: `cacando()` e `fugindo()` são reutilizados pelas subclasses.
- **Ordem de herança**: como a classe filha escolhe métodos quando herda de mais de um pai.

### Classes

- `Animal(nome)`: classe base com atributo `nome`.
- `Predador(Animal)`: adiciona o método `cacando()`.
- `Presa(Animal)`: adiciona o método `fugindo()`.
- `Coelho(Presa)`, `Tigre(Predador)`, `Golfinho(Predador, Presa)`.

### Exemplo de uso

No arquivo `Aula6/main.py`, são criadas instâncias e chamados métodos herdados:

```python
coelho1 = Coelho("Bunny")
tigre1 = Tigre("Leo")
golfinho1 = Golfinho("Billy")

coelho1.fugindo()
tigre1.cacando()
golfinho1.cacando()
```

### Aprendizado

- como combinar herança múltipla e herança de multinível
- como reutilizar métodos de classes pai
- como classes podem herdar comportamentos de mais de um ancestral

- **Especialização**: cada subclasse adiciona seus próprios atributos e métodos.
- **Polimorfismo**: métodos específicos de cada subclasse (`trabalhar`, `comprar`).
- **Encapsulamento de dados**: uso de atributos como `saldo` para controlar estado.

### Classes

- `Pessoa`: classe base com `nome`, `idade` e método `apresentar()`.
- `Funcionario`: subclasse que adiciona `cargo` e método `trabalhar()`.
- `Cliente`: subclasse que adiciona `saldo` e método `comprar()` com validação.

### Exemplo de uso

No arquivo `Aula5/main.py`, são criados funcionários e clientes, demonstrando como cada um utiliza métodos específicos:

```python
f1 = Funcionario("Maria", 38, "Gerente de contas")
f1.apresentar()
f1.trabalhar()

c1 = Cliente("Arthur", 16, 200)
c1.apresentar()
c1.comprar(300)

c2 = Cliente("José", 31, 50)
c2.apresentar()
c2.comprar(30)
```

### Aprendizado

- Como usar `super()` para reutilizar código da classe pai
- Como criar subclasses especializadas com atributos e métodos próprios
- Como validar operações (ex: verificar saldo antes de comprar)
- Como organizar hierarquias de classes para diferentes tipos de objetos

# Aula 7

## Sistema de Escola com Polimorfismo e `super()`

Nesta aula, desenvolvemos um sistema de escola que utiliza herança e polimorfismo para representar diferentes membros da comunidade escolar.

### Conceitos abordados

- **Classe base**: `Escola` contém atributos comuns (`nome`, `idade`, `status`) e métodos reutilizáveis.
- **Polimorfismo**: cada subclasse (`Aluno`, `Professor`, `Assistente`) sobrescreve o método `apresentar()` com sua própria implementação.
- **super()**: usado para chamar métodos da classe pai dentro das subclasses.
- **Expressões ternárias**: uso de `if-else` compacto para exibir status (`"ATIVO"` ou `"INATIVO"`).

### Classes

- `Escola(nome, idade, status)`: classe base com método `apresentar()` e `verificar_status()`.
- `Aluno(nome, idade, status, ano)`: adiciona atributo `ano` da escola.
- `Professor(nome, idade, status, materia)`: adiciona atributo `materia`.
- `Assistente(nome, idade, status, bloco)`: adiciona atributo `bloco`.

### Exemplo de uso

No arquivo `Aula7/main.py`, são criadas instâncias de cada tipo e chamados métodos polimórficos:

```python
a1 = Aluno(nome="Marcos", idade=12, status=True, ano=8)
a1.apresentar()
a1.verificar_status()

p1 = Professor(nome="João", idade=37, status=True, materia="Matemática")
p1.apresentar()
p1.verificar_status()

ass1 = Assistente(nome="Maria", idade=25, status=False, bloco="Bloco C")
ass1.apresentar()
ass1.verificar_status()
```

### Aprendizado

- Como criar uma classe base e reutilizá-la através de herança
- Como cada subclasse pode personalizar métodos herdados
- Como usar `super()` para chamar métodos da classe pai
- Como representar diferentes papéis (Aluno, Professor, Assistente) em um sistema unificado

# Aula 8

## Polimorfismo com personagens

Nesta aula, trabalhamos polimorfismo com uma lista de personagens de um jogo, cada um com sua própria forma de falar.

### Conceitos abordados

- **Polimorfismo**: diferentes classes implementam o mesmo método `falar()` de formas distintas.
- **Herança**: `Guerreiro`, `Mago` e `Arqueiro` herdam de `Personagens`.
- **Coleções de objetos**: os personagens são agrupados em um conjunto para execução em sequência.

### Classes

- `Personagens`: classe base com o método `falar()` padrão.
- `Guerreiro(Personagens)`: sobrescreve `falar()` com uma fala de guerreiro.
- `Mago(Personagens)`: sobrescreve `falar()` com uma fala de mago.
- `Arqueiro(Personagens)`: sobrescreve `falar()` com uma fala de arqueiro.

### Exemplo de uso

No arquivo `Aula8/main.py`, são criadas instâncias dos personagens e o método `falar()` é chamado para cada um:

```python
personagens = {Guerreiro(), Mago(), Arqueiro()}

for p in personagens:
	p.falar()
```

### Aprendizado

- Como aplicar polimorfismo na prática
- Como sobrescrever métodos em subclasses
- Como organizar objetos diferentes em uma mesma coleção
- Como reaproveitar uma classe base para criar comportamentos especializados

# Aula 9

## Agregação com carros e motores

Nesta aula, estudamos agregação usando um carro que pode receber vários motores.

### Conceitos abordados

- **Agregação**: o objeto `Carro` é formado por objetos `Motor` criados separadamente.
- **Coleção de objetos**: o carro mantém uma lista de motores associados.
- **Reuso de objetos**: o mesmo modelo de motor pode ser inserido em uma estrutura maior.

### Classes

- `Motor(marca, potencia)`: representa um motor com marca e potência.
- `Carro()`: classe que mantém uma lista de motores e permite adicioná-los.

### Exemplo de uso

No arquivo `Aula9/main.py`, são criados motores e adicionados a um carro:

```python
motor_v6 = Motor("Ford", 300)
motor_v8 = Motor("Ferrari", 650)
motor_v12 = Motor("Lamborghini", 950)

carro = Carro()
carro.adicionar_motor(motor_v6)
carro.adicionar_motor(motor_v8)
carro.adicionar_motor(motor_v12)

carro.listar_motores()
```

### Aprendizado

- Como representar agregação entre objetos em Python
- Como armazenar objetos em listas dentro de outra classe
- Como percorrer uma coleção para exibir informações
- Como separar a criação dos componentes da classe principal

