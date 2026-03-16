# 1. Tamanho de strings: Leia duas strings, mostre o conteúdo e o tamanho de cada uma. 
# Informe se possuem o mesmo tamanho e se o conteúdo é igual ou diferente. 
string1 = input("Digite a primeira palavra ou frase: ")
string2 = input("Digite a segunda palavra ou frase: ")

tamanho1 = len(string1)
tamanho2 = len(string2)

print(f"\nString 1: '{string1}' (Tamanho: {tamanho1} caracteres)")
print(f"String 2: '{string2}' (Tamanho: {tamanho2} caracteres)")

# Verificando o tamanho
if tamanho1 == tamanho2:
    print("- As duas strings têm o mesmo tamanho.")
else:
    print("- As duas strings têm tamanhos diferentes.")

# Verificando o conteúdo
if string1 == string2:
    print("- As duas strings possuem o mesmo conteúdo.")
else:
    print("- As duas strings possuem conteúdos diferentes.")


# ==========================================


# 2. Nome ao contrário em maiúsculas: Leia o nome do usuário e mostre-o de trás para frente em letras maiúsculas. 
nome = input("Digite o seu nome: ")

nome_invertido = nome[::-1].upper()

print(f"Nome ao contrário em maiúsculas: {nome_invertido}")


# ==========================================


# 3. Nome na vertical: Solicite o nome do usuário e imprima cada letra em uma linha. 
nome = input("Digite o seu nome: ")

for letra in nome:
    print(letra)


# ==========================================


# 4. Nome em escada: Mostre o nome em formato de escada crescente (F, Fu, Ful...). 
nome = input("Digite o seu nome: ")

for i in range(len(nome)):
    # Imprime do início (0) até à posição atual + 1
    print(nome[:i+1])


# ==========================================


# 5. Escada invertida: Mostre o nome em escada decrescente. 
nome = input("Digite o seu nome: ")

for i in range(len(nome), 0, -1):
    print(nome[:i])


# ==========================================


# 6. Data por extenso: Leia uma data (dd/mm/aaa) e mostre no formato '29 de Outubro de 1973'. 
data = input("Digite uma data no formato dd/mm/aaaa: ")

# O .split('/') corta a string sempre que encontra uma barra, criando uma lista com 3 pedaços
dia, mes, ano = data.split('/')

# Criamos uma lista com os nomes dos meses
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# O índice da lista começa em 0, por isso subtraímos 1 do mês digitado (ex: Mês 1 vira índice 0)
mes_extenso = meses[int(mes) - 1]

print(f"{dia} de {mes_extenso} de {ano}")


# ==========================================


# 7. Contar espaços e vogais: Dada uma frase, conte quantos espaços existem e quantas vezes aparecem as vogais. 
frase = input("Digite uma frase: ").lower() # O .lower() converte tudo para minúsculas para facilitar a verificação

espacos = 0
vogais = 0

for caractere in frase:
    if caractere == ' ':
        espacos += 1
    # Verificamos se a letra atual está dentro do grupo de vogais (incluindo acentuadas)
    elif caractere in "aeiouáéíóúãõâêîôû":
        vogais += 1

print(f"A frase tem {espacos} espaço(s).")
print(f"A frase tem {vogais} vogal(is).")


# ==========================================


# 8. Palíndromo: Leia uma sequência de caracteres e informe se é um palíndromo.
# Um palíndromo é uma palavra ou frase que se lê da mesma forma de trás para a frente (ex: OVO, RADAR).
texto = input("Digite uma palavra ou frase: ")

texto_invertido = texto_limpo[::-1]

if texto_limpo == texto_invertido:
    print(f"'{texto}' é um palíndromo!")
else:
    print(f"'{texto}' não é um palíndromo.")


# ==========================================


# 9. Verificação de CPF: Leia um CPF no formato xxx.xxx.xxx-xx e valide os dígitos verificadores.
cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

cpf_numeros = cpf.replace(".", "").replace("-", "")

if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
    print("Formato de CPF inválido. Certifique-se de que tem 11 números.")
else:
    # Validação do primeiro dígito
    soma = 0
    multiplicador = 10
    # Percorremos os primeiros 9 dígitos do CPF
    for i in range(9):
        soma += int(cpf_numeros[i]) * multiplicador
        multiplicador -= 1
        
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    
    digito_1_valido = str(resto) == cpf_numeros[9]

    # Validação do segundo dígito
    soma = 0
    multiplicador = 11
    # Percorremos os primeiros 10 dígitos do CPF
    for i in range(10):
        soma += int(cpf_numeros[i]) * multiplicador
        multiplicador -= 1
        
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
        
    digito_2_valido = str(resto) == cpf_numeros[10]

    # Verificando se ambos os dígitos estão corretos
    if digito_1_valido and digito_2_valido:
        print("O CPF digitado é VÁLIDO.")
    else:
        print("O CPF digitado é INVÁLIDO.")


# ==========================================


# 10. Número por extenso: Leia um número até 99 e mostre-o por extenso.
numero = int(input("Digite um número entre 0 e 99: "))

# Criamos listas com os nomes dos números
unidades_e_especiais = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
                        "dez", "onze", "doze", "treze", "catorze", "quinze", "dezasseis", "dezassete", "dezoito", "dezanove"]

dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

if numero < 0 or numero > 99:
    print("Número fora do limite permitido (0 a 99).")
elif numero < 20:
    # Se for de 0 a 19, basta ir buscar diretamente à primeira lista
    print(unidades_e_especiais[numero])
else:
    dezena_num = numero // 10
    unidade_num = numero % 10
    
    if unidade_num == 0:
        print(dezenas[dezena_num])
    else:
        print(f"{dezenas[dezena_num]} e {unidades_e_especiais[unidade_num]}")


# ==========================================


# 11. Jogo da Forca: Desenvolva um jogo simples da forca usando uma lista de palavras.

palavra_secreta = "ALGORITMO"
letras_acertadas = ["_"] * len(palavra_secreta) # Cria uma lista de "_" com o tamanho da palavra

erros = 0
max_erros = 6
acertou = False

print("Bem-vindo ao Jogo da Forca!")

while erros < max_erros and not acertou:
    print("\nPalavra: ", " ".join(letras_acertadas))
    tentativa = input("Digite uma letra: ").strip().upper()
    
    if tentativa in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == tentativa:
                letras_acertadas[i] = tentativa
    else:
        erros += 1
        print(f"Errou! Faltam {max_erros - erros} tentativas.")
        
    if "_" not in letras_acertadas:
        acertou = True

if acertou:
    print(f"\nParabéns! Descobriu a palavra: {palavra_secreta}")
else:
    print(f"\nPerdeu... A palavra era: {palavra_secreta}")

# ==========================================


# 12. Corrigir telefone: Leia um telefone com 7 ou 8 dígitos e ajuste adicionando o '3' se necessário.
telefone = input("Digite o número de telefone (7 ou 8 dígitos): ")

telefone = telefone.replace("-", "") # Remove o traço caso o utilizador digite

tamanho = len(telefone)

if tamanho == 7:
    telefone_corrigido = "3" + telefone
    print(f"Telefone original: {telefone}")
    print(f"Telefone corrigido (8 dígitos): {telefone_corrigido[:4]}-{telefone_corrigido[4:]}")
elif tamanho == 8:
    print(f"Telefone original já tem 8 dígitos: {telefone[:4]}-{telefone[4:]}")
else:
    print("Número de telefone inválido. Deve ter 7 ou 8 dígitos.")


# ==========================================


# 13. Palavra embaralhada: Mostre uma palavra com letras embaralhadas e permita que o usuário adivinhe.

palavra_correta = "PYTHON"
palavra_embaralhada = "NTOYHP"

print("Bem-vindo ao Jogo da Palavra Embaralhada!")
print(f"Adivinhe a palavra: {palavra_embaralhada}")

tentativa = input("Qual é a sua resposta? ").strip().upper()

if tentativa == palavra_correta:
    print("Parabéns, acertou em cheio!")
else:
    print(f"Que pena, errou. A palavra correta era: {palavra_correta}")

# ==========================================


# 14. Leet Speak: Leia um texto e converta para a escrita estilo leet (ex: 1337).
texto = input("Digite um texto para converter em Leet Speak: ")

texto_leet = texto.upper()
texto_leet = texto_leet.replace("A", "4")
texto_leet = texto_leet.replace("E", "3")
texto_leet = texto_leet.replace("I", "1")
texto_leet = texto_leet.replace("O", "0")
texto_leet = texto_leet.replace("T", "7")
texto_leet = texto_leet.replace("S", "5")

print(f"Texto original: {texto}")
print(f"Texto em Leet Speak: {texto_leet}")
