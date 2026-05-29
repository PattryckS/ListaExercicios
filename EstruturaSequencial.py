# 1. Faça um programa que mostre a mensagem: 'Alô mundo'.
print("Alô mundo")


# ==========================================


# 2. Faça um programa que peça um número e então mostre a mensagem: O número informado foi [número].
numero = input("Digite um número: ")
print(f"O número informado foi {numero}")


# ==========================================


# 3. Faça um programa que peça dois números e imprima a soma.
# Utilizamos o float() para permitir que o usuário digite números com vírgula (decimais)
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2

print(f"A soma dos números é: {soma}")


# ==========================================


# 4. Faça um programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

# Os parênteses garantem que a soma seja feita antes da divisão por 4
media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média do aluno é: {media}")


# ==========================================


# 5. Faça um programa que converta metros para centímetros.
# Sabendo que 1 metro tem 100 centímetros, basta multiplicar por 100.
metros = float(input("Digite uma medida em metros: "))

centimetros = metros * 100

print(f"{metros} metros equivalem a {centimetros} centímetros.")


# ==========================================


# 6. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
# A fórmula da área do círculo é: pi vezes o raio ao quadrado.
# Como estamos no início, vamos usar o valor aproximado de pi como 3.14.
raio = float(input("Digite o raio do círculo: "))
pi = 3.14

# Em Python, usamos ** para calcular a potência (elevado ao quadrado)
area = pi * (raio ** 2)

print(f"A área do círculo é: {area}")


# ==========================================


# 7. Faça um programa que calcule a área de um quadrado e mostre o dobro desta área.
# A área do quadrado é o lado vezes ele mesmo (lado * lado).
lado = float(input("Digite o tamanho do lado do quadrado: "))

area = lado * lado
dobro_da_area = area * 2

print(f"A área do quadrado é: {area}")
print(f"O dobro desta área é: {dobro_da_area}")


# ==========================================


# 8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o salário total do mês.
valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou neste mês? "))

salario_total = valor_hora * horas_trabalhadas

print(f"O seu salário total neste mês será de: R$ {salario_total}")


# ==========================================


# 9. Faça um programa que peça a temperatura em Fahrenheit e converta para Celsius. 
# Fórmula: C = 5 * ((F-32)/9)
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# A conta segue exatamente a fórmula do enunciado
celsius = 5 * ((fahrenheit - 32) / 9)

print(f"A temperatura de {fahrenheit} Fahrenheit equivale a {celsius} graus Celsius.")


# ==========================================


# 10. Faça um programa que peça a temperatura em Celsius e converta para Fahrenheit. 
# Fórmula: F = (C * 9/5) + 32.
celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"A temperatura de {celsius} graus Celsius equivale a {fahrenheit} Fahrenheit.")


# ==========================================


# 11. Peça dois números inteiros e um número real.
# Calcule: (a) o produto do dobro do primeiro com metade do segundo;
# (b) a soma do triplo do primeiro com o terceiro; (c) o terceiro elevado ao cubo.
inteiro1 = int(input("Digite o primeiro número inteiro: "))
inteiro2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real (com casas decimais): "))

calculo_a = (2 * inteiro1) * (inteiro2 / 2)
calculo_b = (3 * inteiro1) + real
calculo_c = real ** 3

print(f"a) Produto do dobro do primeiro com metade do segundo: {calculo_a}")
print(f"b) Soma do triplo do primeiro com o terceiro: {calculo_b}")
print(f"c) O terceiro elevado ao cubo: {calculo_c}")


# ==========================================


# 12. Converta um valor em Gigabytes para Megabytes. Fórmula: MB = GB * 1024.
gb = float(input("Digite o valor em Gigabytes (GB): "))

mb = gb * 1024

print(f"{gb} GB equivalem a {mb} MB.")


# ==========================================


# 13. Converta um valor em Gigabytes para Megabytes e Kilobytes.
gb = float(input("Digite o valor em Gigabytes (GB): "))

mb = gb * 1024
# Sabendo que 1 MB tem 1024 KB
kb = mb * 1024

print(f"{gb} GB equivalem a {mb} MB e a {kb} KB.")


# ==========================================


# 14. Um pescador paga multa de R$4,00 por quilo excedente caso ultrapasse 50 kg de peixes.
# Faça um programa que calcule excesso e multa.
peso_peixes = float(input("Digite a quantidade de peixes pescados (em kg): "))

excesso = 0
multa = 0

# Usamos um 'if' simples para verificar se passou do limite
if peso_peixes > 50:
    excesso = peso_peixes - 50
    multa = excesso * 4.00

print(f"Peso total: {peso_peixes} kg")
print(f"Excesso de peso: {excesso} kg")
print(f"Valor da multa a pagar: R$ {multa:.2f}")


# ==========================================


# 15. Faça um programa que calcule o salário com descontos: IR (11%), INSS (8%) e Sindicato (5%).
# Mostrar salário bruto e líquido.
valor_hora = float(input("Quanto ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas trabalhou no mês? "))

salario_bruto = valor_hora * horas_trabalhadas

# Calculando os descontos (multiplicar pela percentagem dividida por 100)
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"- IR (11%): R$ {ir:.2f}")
print(f"- INSS (8%): R$ {inss:.2f}")
print(f"- Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")


# ==========================================


# 16. Uma loja de tintas precisa calcular quantas latas comprar.
# 1 litro cobre 3 m2, lata tem 18 litros e custa R$80.

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Quantos litros de tinta precisamos?
litros_necessarios = area / 3

# Usamos // para pegar apenas a parte inteira (ex: 2.5 vira 2)
latas_necessarias = int(litros_necessarios // 18)

# Usamos % (resto da divisão) para ver se sobrou alguma tinta fora das latas inteiras
if litros_necessarios % 18 > 0:
    latas_necessarias = latas_necessarias + 1 # Compramos uma lata extra para o que faltou

preco_total = latas_necessarias * 80.00

print(f"Precisará de {latas_necessarias} lata(s) de 18L.")
print(f"O preço total será de R$ {preco_total:.2f}")


# ==========================================


# 17. Versão avançada da tinta: 1 litro cobre 6 m2. Lata 18L (R$80) e galão 3,6L (R$25).
# Calcular melhor opção com 10% de folga.

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Adicionamos 10% de folga à área (multiplicar por 1.1)
area_com_folga = area * 1.10
litros_necessarios = area_com_folga / 6

print(f"\nLitros necessários (com 10% de folga): {litros_necessarios:.2f} L")


# --- Opção 1: Comprar apenas latas de 18L ---
latas_18 = int(litros_necessarios // 18)
if litros_necessarios % 18 > 0:
    latas_18 = latas_18 + 1
    
preco_apenas_latas = latas_18 * 80.00
print(f"Opção 1 - Apenas latas de 18L: {latas_18} lata(s) -> R$ {preco_apenas_latas:.2f}")


# --- Opção 2: Comprar apenas galões de 3.6L ---
galoes_36 = int(litros_necessarios // 3.6)
if litros_necessarios % 3.6 > 0:
    galoes_36 = galoes_36 + 1
    
preco_apenas_galoes = galoes_36 * 25.00
print(f"Opção 2 - Apenas galões de 3.6L: {galoes_36} galão(ões) -> R$ {preco_apenas_galoes:.2f}")


# --- Opção 3: Misturar latas e galões para ficar mais barato ---
# Pegamos o máximo de latas inteiras possíveis
latas_mistura = int(litros_necessarios // 18)

# Vemos quanto sobrou de tinta para colocar nos galões menores
litros_restantes = litros_necessarios - (latas_mistura * 18)

# Calculamos os galões para essa tinta que sobrou
galoes_mistura = int(litros_restantes // 3.6)
if litros_restantes % 3.6 > 0:
    galoes_mistura = galoes_mistura + 1

preco_mistura = (latas_mistura * 80.00) + (galoes_mistura * 25.00)

print(f"Opção 3 - Mistura (Latas + Galões): {latas_mistura} lata(s) e {galoes_mistura} galão(ões) -> R$ {preco_mistura:.2f}")


# ==========================================


# 18. Faça um programa que calcule o tempo aproximado de download de um ficheiro dado o seu
# tamanho (MB) e velocidade da internet (Mbps).
tamanho_mb = float(input("Digite o tamanho do ficheiro em MB: "))
velocidade_mbps = float(input("Digite a velocidade do link de Internet em Mbps: "))

# 1 Byte = 8 bits, portanto precisamos converter a velocidade para Megabytes por segundo (MBps)
velocidade_MBps = velocidade_mbps / 8
tempo_segundos = tamanho_mb / velocidade_MBps

# Convertendo os segundos para minutos
tempo_minutos = tempo_segundos / 60

print(f"O tempo aproximado de download será de {tempo_minutos:.2f} minutos.")
