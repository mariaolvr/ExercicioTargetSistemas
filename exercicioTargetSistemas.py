# calculo variavel SOMA
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)



# sequencia de Fibonacci
def fibonacci(n):
    """Gera a sequencia de Fibonacci até o numero 'n'."""
    a, b = 6, 9
    while a < n:
        a, b = b, a + b
    return a == n

# Entrada do usuario
numero = int(input("Digite um número: "))

# Verifica se o numero pertence a sequencia
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")



# Analise de faturamento
import json
import os

diretorio = r'C:\Users\maria'
arquivo_json = 'dados.json'

# Constrói o caminho completo do arquivo
caminho_arquivo = os.path.join(diretorio, arquivo_json)

# Carrega os dados de faturamento
with open(caminho_arquivo, 'r') as f:
    faturamento_diario = json.load(f)

# Filtra os dias com faturamento maior que 0
valores = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

# Calcula o menor e o maior valor de faturamento
menor_valor = min(valores)
maior_valor = max(valores)

# Calcula a média mensal (ignorando dias sem faturamento)
media_mensal = sum(valores) / len(valores)

# Conta os dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

# Imprime os resultados
print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")




# Percentual de representacao por estado
# Valores de faturamento por estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o faturamento total
faturamento_total = sum(faturamento_estados.values())

# Calcula o percentual de representação de cada estado
percentual_estados = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

# Imprime os resultados
for estado, percentual in percentual_estados.items():
    print(f"{estado}: {percentual:.2f}%")




# String de entrada 
string = "Gostaria de saber o faturamento atual."

# Inverte a string manualmente
string_invertida = ""
for caractere in string:
    string_invertida = caractere + string_invertida

# Imprime a string invertida
print("String original:", string)
print("String invertida:", string_invertida)
