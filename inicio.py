#Conceitos Basicos 
#1.Faça um Programa que peça um número e então mostre a mensagem:->O número informado foi [número].
'''n= int(input("digite um numero "))
print(f"o numero digitado foi: {n}")'''

#2.Faça um Programa que peça dois números e imprima a soma.
'''n1=int(input("digite o primeiro numero "))
n2=int(input("digite o segundo numero "))
soma=n1+n2
print("a soma vale", soma)'''

#3.Faça um Programa que peça a temperatura em graus Celsius,transforme e mostre em graus Fahrenheit.
'''t=int(input("digite a temperatura em Celsius "))
f= t * (9/5) + 32
print(f"a temperatura em F é : {f}")'''

#4.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
'''valor=float(input("digite quanto você recebe por hora "))
hora=float(input("quantas horas você trabalha "))
salario = valor * hora 
print(f"o valor do seu salario é R$ : {salario}")'''


#Estrutura de Repetição
#1.Faça um Programa que peça dois números e imprima o maior deles.
'''n1=int(input("digite o primeiro numero "))
n2=int(input("digite o segundo numero "))
if(n1 > n2):
    maior=n1
else:
    maior=n2

print(f"o maior numero foi : {maior}") '''

#2.Faça um Programa que pergunte em que turno você estuda.Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
#Imprima a mensagem "BomDia!" ,"BoaTarde!" ou "BoaNoite!" ou "Valor Inválido!",conforme o caso.
'''t=input("qual turno você estuda ? M-matutino, V-vespertino, N-noturno ")
if t == "M":
    mensagem = "Bom Dia"
elif t == "V":
    mensagem = "Boa Tarde"
elif t == "N":
    mensagem = "Boa Noite"
else :
    mensagem = "valor invalido"
print(mensagem)'''

#3.Faça um programa que peça uma nota,entre zero e dez.Mostre uma mensagem caso o valor seja inválido 
#e continue pedindo até que o usuário informe um valor válido.
'''while True:
    nota= int(input("digite uma nota entre 0 e 10 "))
    if 0 <= nota <= 10:
      break
    else:
       print("valor invalido , tente novamente ")

print("nota valida ", nota)'''


#Listas, Tuplas e Dicionários
#1."Faça um Programa que peça as quatro notas de 10 alunos,calcule e armazene numa lista a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0.
'''listaNotas=[]
listaMedias=[]
quantidadeAlunos=2
quantidadeNotas=2

for aluno in range(quantidadeAlunos):
    listaNotas.append([])
    for nota in range(quantidadeNotas):
        listaNotas[aluno].append(
            float(
                input(f"digite a nota {nota} do aluno {aluno} ")
            )
        )

for notas in listaNotas:
    listaMedias.append(
        sum(notas)/ len(notas)
    )

alunos_aprovados= sum(1 for media in listaMedias if media >= 7.0)
print(f"numero de alunos com media maior ou igual a 7.0 : {alunos_aprovados}")'''

#2.Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.Dica:lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
'''nome=input("digite seu nome ")
letras = []
for i in range (len(nome)-1, -1, -1):
    letras.append(nome[i].upper())

print(''.join(letras))'''

#3.Escreva um programa em Python onde todos os valores em um dicionário são emitidos.Se sim,imprima True.
# Caso contrário,imprima Falso.
'''dicionario = {"uva":"fruta","apartamento":"imovel","python":"programa"}
print(dicionario)
valores_emitidos= all(valor for valor in dicionario.values())

if valores_emitidos:
    print("True")
else:
    print("False")'''

#4."Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.As perguntas são:"
#"Telefonou para a vítima?""
#""Esteve no local do crime?""
#""Mora perto da vítima?""
#""Devia para a vítima?""
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como""Suspeita"",entre 3 e 4 como""Cúmplice"
#e 5 como""Assassino"".Caso contrário,ele será classificado como""Inocente"".
'''respostas_positivas= 0
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

for pergunta in perguntas :
    resposta = input(pergunta + "(sim/nao): ").lower()
    if resposta =="sim":
        respostas_positivas +=1

if respostas_positivas == 5:
    classificacao= "assassino"
elif respostas_positivas >= 3:
    classificacao= "cumplice"
elif respostas_positivas >= 2:
    classificacao= "suspeito"
else:
    classificacao= "inocente"
print(classificacao)'''


#Funções
#1.Faça um programa,com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 
'''def programa (n1, n2, n3):
    soma = n1 + n2 + n3
    print(soma)
programa(5,10,20)'''

#2.Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127->721. 
'''def reverso(numero):
    numero_str = str(numero)
    reverse = []

    for n in range(len (numero_str)-1, -1, -1):
        reverse.append(numero_str[n])
    reverse = int(''.join(reverse))
    return reverse

num = int(input("digite um numero "))
print(reverso(num))'''

#3.Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção,
# crie uma função.Crie uma terceira, que é um menu para o usuário escolher a opção desejada,onde esse menu chama a função de conversão correta.
'''def celsiusFahrenheit(grausC):
    return (grausC*9/5)+32
def fahrenheitCelsius(grausF):
    return (grausF-32) *5/9

def menu():
    print("escolha uma opção ")
    print("1. converter de Celsius para Fahrenheit ")
    print("2. converter de Fahrenheit para Celsius ")
    escolha = input("digite a opção desejada ")
    return escolha

escolha = menu()
if escolha  == "1":
    grausC = float(input("digite a temperatura em Celsius "))
    Fahrenheit = celsiusFahrenheit(grausC)
    print(f"valor em Fahrenheit: {Fahrenheit}")
elif escolha == "2":
    grausF = float(input("digite a temperatura em Fahrenheit "))
    celsius = fahrenheitCelsius(grausF)
    print(f"valor em celsius : {celsius}")
else:
    print("opção invalida ")'''

#1.Crie um programa que leia quanto dinheiro uma pessoa tem na carteira,e calcule quanto poderia comprar de cada moeda estrangeira.
# Considere a tabela de conversão abaixo: 
#Dólar Americano:R$4,91
#Peso Argentino:R$0,02
#Dólar Australiano:R$3,18
#Dólar Canadense:R$3,64
#Franco Suiço:R$0,42
#Euro:R$5,36
#Libra esterlina:R$6,21.
'''valor= input("digite valor em real ")
print(f"dolar americano : {float(valor)/4.91}")
print(f"peso argentino : {float(valor)/0.02}")
print(f"dolar australiano : {float(valor)/3.18}")
print(f"dolar canadense : {float(valor)/3.64}")
print(f"franco suiço : {float(valor)/0.42}")
print(f"euro : {float(valor)/5.36}")
print(f"libra esterlina : {float(valor)/6.21}")'''

#2.Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar,sabendo que o carro custa R$80,00 por dia e R$0,20 por km rodado.
'''percorrido= float(input("digite km percorridos "))
alugado= float(input("quantidade de dias alugados "))

custo_km = 0.20
custo_dia = 80.00
print(f"valor a ser pago : {(percorrido*custo_km)+ (alugado*custo_dia)}")'''

#3.Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário.Se o salário for até R$1000,00 o funcionário terá 20% de aumento.
#Entre R$1001,00 até R$2800,00 o funcionário terá 10% de aumento.Acima de R$2801,00 o funcionário terá 5% de aumento.
'''salario=float(input("digite seu salario "))
if salario <= 1000:
    print(f"o novo salario é {salario*1.2}")
elif salario <= 2800:
    print(f"o novo salario é {salario*1.1}")
else:
    print(f"o novo salario é {salario*1.05}")'''

#4.Crie um programa que tenha a função leiaInt(),que vai funcionar de forma semelhante à funçãoinput() do Python,só que fazendo avalidação para aceitar 
# apenas um valor númerico. 
'''def leiaInt():
    while True:
        try:
            return int(input("digite um valor inteiro "))
        except ValueError:
            print("valor invalido")

numero = leiaInt()
print(f"o numero digitado foi : {numero}")'''





