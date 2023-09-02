## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

# exercicio 03

'''def calcular_media(valores):
    tamanho = 0
    soma = 0.0
    for valor in valores:
        soma += valor
        tamanho += 1
    media = soma / tamanho
    return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False
    else:
        valores.append(float(valor))

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))'''

# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
# Crie uma instância da classe carro.
# Faça o carro "andar" utilizando os métodos da sua classe.
# Faça o carro "parar" utilizando os métodos da sua classe.

# exercicio 01

'''class Carro:
    def __init__(self,cor,modelo):
        self.cor = cor
        self.modelo = modelo 
        self.ligado = False
        self.velocidade = 0.0 
        self.limite_velocidade = 120.0

    def liga(self):
        self.ligado = True
    
    def desliga(self):
        self.ligado = False 
        self.velocidade = 0.0 

    def acelera(self):
        if self.ligado == False:
            return
        
        if self.velocidade < self.limite_velocidade:
            self.velocidade +=5

    def desacelera(self):
        if self.ligado == False:
            return 
        if self.velocidade > 0:
            self.velocidade = self.velocidade - 5

    def __str__(self):
        ligado_str = "ligado" if self.ligado == True else "desligado"
        return f"Carro {self.modelo} de cor {self.cor} está {ligado_str}, com velocidade de {self.velocidade}"

carro= Carro("azul","honda")
print(carro)

carro.liga()
print(carro)

for i in range(5):
    carro.acelera()
print(carro)

carro.desliga()
print(carro)'''

# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.
# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.
# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

# exercicio 02

'''def Apresentacao():
    espacador = '*' * 40
    print(espacador, '\nBoas-vindas ao Banco Delas\n', espacador, '\nCadastre-se:\n')


Apresentacao()


# Criando classe
# Atributos: Número da conta, nome do titular, saldo disponível
class ContaCorrente():

    # Construtor de classe
    def __init__(self, nome_titular, senha, id_conta,saldo_cc):
        self.nome_titular = nome_titular
        self.senha = senha
        self.id_conta = id_conta
        self.saldo_cc = 0
    

    # Métodos: sacar, depositar na Poupança
    def sacar(self):
        valor = int(input('Quanto deseja sacar: R$ '))
        if self.saldo_cc >= valor or self.saldo_cc >= 0:
            self.saldo_cc += valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficente.')

    def depositar(self):
        valor = int(input('Quanto deseja depositar: R$ '))
        self.saldo_poup += valor
        print('Depósito realizado com sucesso!')

    def extrato(self):
        espacador = '*' * 20
        print()
        print(espacador)
        print('Titular da conta: ', nome_titular)
        print('Conta Corrente nº: ', id_conta)
        print('Seu saldo atual é R$ ', self.saldo_cc, ',00')
        print(espacador)
        print()

        espacador = '*' * 20
        print(espacador)
        print('Titular da conta: ', nome_titular)
        print('Conta POupança nº: ', id_conta)
        print('Seu saldo atual é R$ ', self.saldo_poup, ',00')
        print(espacador)
        print()

    def get_saldo(self, senha):
        self.senha = senha
        acesso = int(input('Senha: '))
        if self.senha == acesso:
            conta.extrato()
        elif self.senha != acesso:
            print('Acesso negado. Tente novamente.')


# Criando a classe Conta Poupança (sub-classe)
class ContaPoupanca(ContaCorrente):

    def __init__(self, nome_titular, id_conta, saldo_cc, saldo_poup):
        ContaCorrente.__init__(self, nome_titular, senha, id_conta, saldo_cc)
        self.nome_titular = nome_titular
        self.senha = senha
        self.id_conta = id_conta
        self.saldo_cc = 0
        self.saldo_poup = primeiro_dep
        print("Conta cadastrada com sucesso!")

    def resgatar(self):
        valor = int(input('Quanto deseja resgatar: R$ '))
        self.saldo_poup -= valor
        self.saldo_cc += valor
        print('Resgate realizado com sucesso!')


# Solicitando informações iniciais e cadastrando usuário
nome_titular = str(input('Informe seu nome e sobrenome: '))
senha = int(input('Favor cadastrar uma senha de 4 dígitos: '))

import random

id_conta = random.randint(000, 1000)

primeiro_dep = int(input('Seu saldo atual é R$0,00. Realize seu primeiro depósito: R$ '))

conta = ContaPoupanca(nome_titular, id_conta, 0, primeiro_dep)

# Automatizando interação do usuário com a conta
while (True):
    operacoes = int(input(
        'Deseja movimentar sua conta?\nOperações disponíveis (1-Sacar, 2-Depositar, 3-Resgatar, 4-Extrato, 5-Sair): '))

    if operacoes == 1:
        conta.sacar()
    elif operacoes == 2:
        conta.depositar()
    elif operacoes == 3:
        conta.resgatar()
    elif operacoes == 4:
        conta.get_saldo(senha)
    elif operacoes == 5:
        print('Operação finalizada.')
        break
    else:
        print('Valor inválido.')'''