CONSTANTE_BONUS = 1000      #Boa prática usar constantes em maiúsculas

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o bônus recebido: "))

# 4) Calcule o valor do bônus final
bonus_final = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"O usuário {nome_usuario} possui o bonus no valor de {bonus_final}.")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
""""
Não há tratativas para evitar erros de entrada de dados, como por exemplo:
- usuário pode não digitar o nome, ou preencher com valores inválidos
- usuário pode digitar o salário e bonus por extenso
"""
