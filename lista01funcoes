# Exercício 1: Validação de Strings e Parâmetros

def valida_string(texto, minimo=1, maximo=100):
    tamanho = len(texto)
        if tamanho >= minimo and tamanho <= maximo:
        return True
    else:
        return False

# ==========================================

# Exercício 2: Cálculo de Imposto (Funções com Retorno)

def soma_imposto(taxa_imposto, custo):
    valor_imposto = custo * (taxa_imposto / 100)
    
    valor_final = custo + valor_imposto
    
    return valor_final

# Programa Principal 

custo_produto = float(input("Digite o custo do produto: € "))
taxa_produto = float(input("Digite a taxa de imposto (em %): "))

resultado = soma_imposto(taxa_produto, custo_produto)

print(f"\nO valor final do produto (com imposto) é: € {resultado:.2f}")
