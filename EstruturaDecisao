# Exercício 01 Faça um programa que peça dois números e imprima o maior deles.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O maior número é: {numero1}")
elif numero2 > numero1:
    print(f"O maior número é: {numero2}")
else:
    print("Os dois números são iguais.")


# ==========================================


# Exercício 02 Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = float(input("Digite um valor: "))

if valor >= 0:
    print("O valor é positivo.")
else:
    print("O valor é negativo.")


# ==========================================


# Exercício 03 Faça um programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: 
# F - Feminino 
# M - Masculino 
# Sexo Inválido. 
sexo = input("Digite o sexo (F ou M): ").strip().upper()

if sexo == "F":
    print("F - Feminino")
elif sexo == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido.")


# ==========================================


# Exercício 04 Faça um programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: ").strip().lower()

if letra in ['a', 'e', 'i', 'o', 'u']:
    print("A letra digitada é uma vogal.")
elif letra.isalpha(): 
    # Verifica se realmente é uma letra do alfabeto e não um número ou símbolo
    print("A letra digitada é uma consoante.")
else:
    print("Entrada inválida. Por favor, digite apenas uma letra.")


# ==========================================


# Exercício 05 Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar: 
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
# A mensagem "Reprovado", se a média for menor do que sete; 
# A mensagem "Aprovado com Distinção", se a média for igual a dez. 
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# Exercício 06 Faça um programa que leia três números e mostre o maior deles. 
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(f"O maior número é: {maior}")


# ==========================================


# Exercício 07 Faça um programa que leia três números e mostre o maior e o menor deles. 
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

maior = n1
menor = n1

# Verificando o maior
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

# Verificando o menor
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")


# ==========================================


# Exercício 08 Faça um programa que pergunte o preço de três produtos e informe 
# qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
preco1 = float(input("Digite o preço do primeiro produto: R$ "))
preco2 = float(input("Digite o preço do segundo produto: R$ "))
preco3 = float(input("Digite o preço do terceiro produto: R$ "))

if preco1 <= preco2 and preco1 <= preco3:
    print("Você deve comprar o primeiro produto.")
elif preco2 <= preco1 and preco2 <= preco3:
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")


# ==========================================


# Exercício 09 Faça um programa que leia três números e mostre-os em ordem decrescente. 
v1 = float(input("Digite o primeiro número: "))
v2 = float(input("Digite o segundo número: "))
v3 = float(input("Digite o terceiro número: "))

if v1 >= v2 and v1 >= v3:
    if v2 >= v3:
        print(f"Ordem decrescente: {v1}, {v2}, {v3}")
    else:
        print(f"Ordem decrescente: {v1}, {v3}, {v2}")
elif v2 >= v1 and v2 >= v3:
    if v1 >= v3:
        print(f"Ordem decrescente: {v2}, {v1}, {v3}")
    else:
        print(f"Ordem decrescente: {v2}, {v3}, {v1}")
else:
    if v1 >= v2:
        print(f"Ordem decrescente: {v3}, {v1}, {v2}")
    else:
        print(f"Ordem decrescente: {v3}, {v2}, {v1}")


# ==========================================


# Exercício 10 Faça um programa que pergunte em que turno você estuda. Peça para digitar: 
# M- Matutino 
# V - Vespertino 
# N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 
turno = input("Em que turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ").strip().upper()

if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")

# ==========================================


# Exercício 11 As Organizações Tabajara resolveram dar um aumento de salário aos
# seus colaboradores e lhe contrataram para desenvolver o programa que calculará
# os reajustes. 
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
# seguinte critério, baseado no salário atual: 
# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10% 
# salários de R$ 1500,00 em diante: aumento de 5% 
# Após o aumento ser realizado, informe na tela: 
# o salário antes do reajuste; 
# o percentual de aumento aplicado; 
# o valor do aumento; 
# o novo salário, após o aumento. 

salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

if salario_atual <= 280.00:
    percentual = 20
elif salario_atual <= 700.00:
    percentual = 15
elif salario_atual <= 1500.00:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + valor_aumento

print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")


# ==========================================


# Exercício 12 Faça um programa para o cálculo de uma folha de pagamento,
# sabendo que os descontos são do Imposto de Renda, que depende do salário
# bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
# 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas 
# trabalhadas no mês. 
# Desconto do IR: 
# Salário Bruto até 900 (inclusive) - isento 
# Salário Bruto até 1500 (inclusive) - desconto de 5% 
# Salário Bruto até 2500 (inclusive) - desconto de 10% 
# Salário Bruto acima de 2500 - desconto de 20% 

valor_hora = float(input("Digite o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

# Cálculo do IR
if salario_bruto <= 900:
    percentual_ir = 0
elif salario_bruto <= 1500:
    percentual_ir = 5
elif salario_bruto <= 2500:
    percentual_ir = 10
else:
    percentual_ir = 20

desconto_ir = salario_bruto * (percentual_ir / 100)
desconto_inss = salario_bruto * 0.10 # Baseado no exemplo do enunciado (10%)
desconto_sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
total_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print(f"\nSalário Bruto: ({valor_hora} * {horas_trabalhadas}): R$ {salario_bruto:.2f}")
print(f"(-) IR ({percentual_ir}%): R$ {desconto_ir:.2f}")
print(f"(-) INSS (10%): R$ {desconto_inss:.2f}")
print(f"(-) Sindicato (3%): R$ {desconto_sindicato:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Liquido: R$ {salario_liquido:.2f}")


# ==========================================


# Exercício 13 Faça um programa que leia um número e exiba o dia correspondente
# da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer
# valor inválido. 

dia = int(input("Digite um número para o dia da semana (1 a 7): "))

if dia == 1:
    print("1 - Domingo")
elif dia == 2:
    print("2 - Segunda-feira")
elif dia == 3:
    print("3 - Terça-feira")
elif dia == 4:
    print("4 - Quarta-feira")
elif dia == 5:
    print("5 - Quinta-feira")
elif dia == 6:
    print("6 - Sexta-feira")
elif dia == 7:
    print("7 - Sábado")
else:
    print("Valor inválido")


# ==========================================


# Exercício 14 Faça um programa que lê as duas notas parciais obtidas por um
# aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo: 
# Entre 9.0 e 10.0 -> A 
# Entre 7.5 e 9.0 -> B 
# Entre 6.0 e 7.5 -> C 
# Entre 4.0 e 6.0 -> D 
# Entre 4.0 e zero -> E 
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
# mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o
# conceito for D ou E. 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if 9.0 < media <= 10.0:
    conceito = "A"
elif 7.5 < media <= 9.0:
    conceito = "B"
elif 6.0 < media <= 7.5:
    conceito = "C"
elif 4.0 < media <= 6.0:
    conceito = "D"
elif 0.0 <= media <= 4.0:
    conceito = "E"
else:
    conceito = "Inválido"

print(f"\nNotas: {nota1} e {nota2}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")

if conceito in ["A", "B", "C"]:
    print("Situação: APROVADO")
elif conceito in ["D", "E"]:
    print("Situação: REPROVADO")
else:
    print("Situação: Notas fora do padrão.")


# ==========================================


# Exercício 15 Faça um programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
# Três lados formam um triângulo quando a soma de quaisquer dois lados for
# maior que o terceiro; 
# Triângulo Equilátero: três lados iguais; 
# Triângulo Isósceles: quaisquer dois lados iguais; 
# Triângulo Escaleno: três lados diferentes; 

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

# Verificando se é um triângulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("\nOs valores formam um triângulo.")
    
    if lado1 == lado2 == lado3:
        print("Tipo: Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Tipo: Triângulo Isósceles")
    else:
        print("Tipo: Triângulo Escaleno")
else:
    print("\nOs valores não podem formar um triângulo.")


# ==========================================

# Exercício 16 Faça um programa que calcule as raízes de uma equação do
# segundo grau, na forma ax2+bx+c. O programa deverá pedir os valores de a, b e c
# e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo
# grau e o programa não deve pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raízes reais.
# Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
# informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raízes reais; informe-as ao
# usuário;

a = float(input("Digite o valor de a: "))

if a == 0:
    print("O valor de 'a' é igual a zero. A equação não é do segundo grau e o programa será encerrado.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("O delta calculado é negativo. A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"O delta é igual a zero. A equação possui apenas uma raiz real: {raiz}")
    else:
        raiz1 = (-b + (delta ** 0.5)) / (2 * a)
        raiz2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"O delta é positivo. A equação possui duas raízes reais: {raiz1} e {raiz2}")


# ==========================================


# Exercício 17 Faça um programa que peça um número correspondente a um
# determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite um ano (ex: 2024): "))

# Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400.
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")


# ==========================================


# Exercício 18 Faça um programa que peça uma data no formato dd/mm/aaaa e
# determine se a mesma é uma data válida.

data_str = input("Digite uma data no formato dd/mm/aaaa: ")

# Separando dia, mês e ano e convertendo para inteiros (assumindo que o usuário digitou no formato correto)
dia_str, mes_str, ano_str = data_str.split('/')
dia = int(dia_str)
mes = int(mes_str)
ano = int(ano_str)

data_valida = False

# Verificando meses com 31 dias
if mes in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= dia <= 31:
        data_valida = True
# Verificando meses com 30 dias
elif mes in [4, 6, 9, 11]:
    if 1 <= dia <= 30:
        data_valida = True
# Verificando fevereiro e anos bissextos
elif mes == 2:
    ano_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    if ano_bissexto:
        if 1 <= dia <= 29:
            data_valida = True
    else:
        if 1 <= dia <= 28:
            data_valida = True

if data_valida:
    print(f"A data {data_str} é VÁLIDA.")
else:
    print(f"A data {data_str} é INVÁLIDA.")


# ==========================================


# Exercício 19 Faça um programa que leia um número inteiro menor que 1000 e
# imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades

numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000 or numero < 0:
    print("Número inválido! O número deve ser positivo e menor que 1000.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas > 0:
        if centenas == 1:
            partes.append("1 centena")
        else:
            partes.append(f"{centenas} centenas")
            
    if dezenas > 0:
        if dezenas == 1:
            partes.append("1 dezena")
        else:
            partes.append(f"{dezenas} dezenas")
            
    if unidades > 0:
        if unidades == 1:
            partes.append("1 unidade")
        else:
            partes.append(f"{unidades} unidades")

    # Juntando as partes com vírgula e "e"
    if len(partes) == 3:
        resultado = f"{partes[0]}, {partes[1]} e {partes[2]}"
    elif len(partes) == 2:
        resultado = f"{partes[0]} e {partes[1]}"
    elif len(partes) == 1:
        resultado = partes[0]
    else:
        resultado = "0 unidades"
        
    print(f"{numero} = {resultado}")


# ==========================================


# Exercício 20 Faça um programa para leitura de três notas parciais de um aluno. O
# programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f"Aprovado com Distinção. Média alcançada: {media:.2f}")
elif media >= 7:
    print(f"Aprovado. Média alcançada: {media:.2f}")
else:
    print(f"Reprovado. Média alcançada: {media:.2f}")


# ==========================================


# Exercício 21 Faça um programa para um caixa eletrônico. O programa deverá
# perguntar ao usuário o valor do saque e depois informar quantas notas de cada
# valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se
# preocupar com a quantidade de notas existentes na máquina.

saque = int(input("Digite o valor do saque (entre R$ 10 e R$ 600): "))

if saque < 10 or saque > 600:
    print("Valor inválido. O saque deve ser entre R$ 10 e R$ 600.")
else:
    notas_100 = saque // 100
    resto = saque % 100
    
    notas_50 = resto // 50
    resto = resto % 50
    
    notas_10 = resto // 10
    resto = resto % 10
    
    notas_5 = resto // 5
    notas_1 = resto % 5
    
    print(f"\nPara sacar a quantia de {saque} reais, o programa fornece:")
    if notas_100 > 0:
        print(f"{notas_100} nota(s) de 100")
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de 50")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de 10")
    if notas_5 > 0:
        print(f"{notas_5} nota(s) de 5")
    if notas_1 > 0:
        print(f"{notas_1} nota(s) de 1")


# ==========================================


# Exercício 22 Faça um programa que peça um número inteiro e determine se ele é
# par ou ímpar. Dica: utilize o operador módulo (resto da divisão).

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


# ==========================================


# Exercício 23 Faça um programa que peça um número e informe se o número é
# inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input("Digite um número: "))

if numero == round(numero):
    print(f"O número {numero} é inteiro.")
else:
    print(f"O número {numero} é decimal.")


# ==========================================


# Exercício 24 Faça um programa que leia 2 números e em seguida pergunte ao
# usuário qual operação ele deseja realizar. O resultado da operação deve ser
# acompanhado de uma frase que diga se o número é:
# par ou ímpar; positivo ou negativo; inteiro ou decimal.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação deseja realizar? (+, -, *, /): ").strip()

valido = True
resultado = 0

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        valido = False
else:
    print("Operação inválida.")
    valido = False

if valido:
    print(f"\nResultado da operação: {resultado}")
    
    # Verificando Par ou Ímpar
    if resultado % 2 == 0:
        print("- O resultado é par.")
    else:
        print("- O resultado é ímpar.")
        
    # Verificando Positivo ou Negativo
    if resultado > 0:
        print("- O resultado é positivo.")
    elif resultado < 0:
        print("- O resultado é negativo.")
    else:
        print("- O resultado é zero (neutro).")
        
    # Verificando Inteiro ou Decimal
    if resultado == round(resultado):
        print("- O resultado é inteiro.")
    else:
        print("- O resultado é decimal.")


# ==========================================


# Exercício 25 Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 1. "Telefonou para a vítima?" 
# 2. "Esteve no local do crime?" 
# 3. "Mora perto da vítima?" 
# 4. "Devia para a vítima?" 
# 5. "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

print("Responda às perguntas abaixo com 'S' para SIM ou 'N' para NÃO:")
p1 = input("1. Telefonou para a vítima? ").strip().upper()
p2 = input("2. Esteve no local do crime? ").strip().upper()
p3 = input("3. Mora perto da vítima? ").strip().upper()
p4 = input("4. Devia para a vítima? ").strip().upper()
p5 = input("5. Já trabalhou com a vítima? ").strip().upper()

respostas_positivas = 0

if p1 == 'S':
    respostas_positivas += 1
if p2 == 'S':
    respostas_positivas += 1
if p3 == 'S':
    respostas_positivas += 1
if p4 == 'S':
    respostas_positivas += 1
if p5 == 'S':
    respostas_positivas += 1

print("\n--- Resultado da Investigação ---")
if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif respostas_positivas == 3 or respostas_positivas == 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")


# ==========================================


# Exercício 26 Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
# Álcool: 
# até 20 litros: desconto de 3% por litro 
# acima de 20 litros: desconto de 5% por litro 
# Gasolina: 
# até 20 litros: desconto de 4% por litro 
# acima de 20 litros: desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
# ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 e o 
# preço do litro do álcool é R$ 1,90. 

litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").strip().upper()

valor_pagar = 0
valido = True

if tipo == 'A':
    preco_litro = 1.90
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_bruto = litros * preco_litro
    valor_pagar = valor_bruto - (valor_bruto * desconto)

elif tipo == 'G':
    preco_litro = 2.50
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_bruto = litros * preco_litro
    valor_pagar = valor_bruto - (valor_bruto * desconto)

else:
    print("Tipo de combustível inválido!")
    valido = False

if valido:
    print(f"Valor a ser pago: R$ {valor_pagar:.2f}")


# ==========================================


# Exercício 27 Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
# Morango: Até 5 Kg -> R$ 2,50 por Kg | Acima de 5 Kg -> R$ 2,20 por Kg 
# Maçã: Até 5 Kg -> R$ 1,80 por Kg | Acima de 5 Kg -> R$ 1,50 por Kg 
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar 
# R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de 
# maçãs adquiridas e escreva o valor a ser pago pelo cliente. 

kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))

# Calculando preço dos morangos
if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

# Calculando preço das maçãs
if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

valor_total = preco_morango + preco_maca
kg_total = kg_morango + kg_maca

# Aplicando desconto se necessário
if kg_total > 8 or valor_total > 25.00:
    valor_total = valor_total - (valor_total * 0.10)

print(f"O valor total a ser pago é: R$ {valor_total:.2f}")


# ==========================================


# Exercício 28 O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira: 
# File Duplo: Até 5 Kg -> R$ 4,90 por Kg | Acima de 5 Kg -> R$ 5,80 por Kg 
# Alcatra: Até 5 Kg -> R$ 5,90 por Kg | Acima de 5 Kg -> R$ 6,80 por Kg 
# Picanha: Até 5 Kg -> R$ 6,90 por Kg | Acima de 5 Kg -> R$ 7,80 por Kg 
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos 
# de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
# Se a compra for feita no cartão Tabajara o cliente receberá ainda um 
# desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo 
# as informações da compra: tipo e quantidade de carne, preço total, tipo de 
# pagamento, valor do desconto e valor a pagar. 

print("Tipos de carne disponíveis:")
print("F - File Duplo")
print("A - Alcatra")
print("P - Picanha")
tipo_carne = input("Digite o tipo de carne desejada (F, A ou P): ").strip().upper()
kg_carne = float(input("Digite a quantidade desejada (em Kg): "))
pagamento = input("Pagamento no cartão Tabajara? (S para Sim, N para Não): ").strip().upper()

nome_carne = ""
preco_total = 0
valido = True

if tipo_carne == 'F':
    nome_carne = "File Duplo"
    if kg_carne <= 5:
        preco_total = kg_carne * 4.90
    else:
        preco_total = kg_carne * 5.80
        
elif tipo_carne == 'A':
    nome_carne = "Alcatra"
    if kg_carne <= 5:
        preco_total = kg_carne * 5.90
    else:
        preco_total = kg_carne * 6.80
        
elif tipo_carne == 'P':
    nome_carne = "Picanha"
    if kg_carne <= 5:
        preco_total = kg_carne * 6.90
    else:
        preco_total = kg_carne * 7.80
        
else:
    print("Tipo de carne inválido.")
    valido = False

if valido:
    desconto = 0
    tipo_pagamento = "Outro"
    
    if pagamento == 'S':
        desconto = preco_total * 0.05
        tipo_pagamento = "Cartão Tabajara"
        
    valor_a_pagar = preco_total - desconto
    
    # Gerando o Cupom Fiscal
    print("\n" + "="*30)
    print("       CUPOM FISCAL")
    print("="*30)
    print(f"Tipo de carne:       {nome_carne}")
    print(f"Quantidade:          {kg_carne:.2f} Kg")
    print(f"Preço total:         R$ {preco_total:.2f}")
    print(f"Tipo de pagamento:   {tipo_pagamento}")
    print(f"Valor do desconto:   R$ {desconto:.2f}")
    print("-" * 30)
    print(f"VALOR A PAGAR:       R$ {valor_a_pagar:.2f}")
    print("="*30)
