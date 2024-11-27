# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# try:
#     num1 = int(input("Digite o primeiro número inteiro: "))
#     num2 = int(input("Digite o segundo número inteiro: "))
#     resultado = num1 + num2
#     print(f"A soma de {num1} e {num2} é igual a {resultado}.")
# except ValueError:
#     print("Por favor, insira números inteiros válidos.")
#Este código só aceita números inteiros no input, para considerar a parte inteira de um número float, seria necessário usar o cast float() no input e
#posteriormente converter os inputs para int().

# # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# try:
#     num = float(input("Digite um número: "))
#     if num < 5:
#         print("O número deve ser maior que 5.")
#         exit()
#     else:
#         resto = num % 5
#         print(f"O resto da divisão de {num} por 5 é {resto}.")
# except ValueError:
#     print("Por favor, insira um número válido.")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# try:
#     num1 = float(input("Digite um número :"))
#     num2 = float(input("Digite outro número: "))
#     resultado = num1 * num2
#     print(f"A multiplicação entre {num1} e {num2} é {resultado}")
# except ValueError:
#     print("Por favor, insira um número válido.")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# try:
#     num1 = int(input("Digite o primeiro número inteiro:"))
#     num2 = int(input("Digite o segundo número inteiro:"))
#     divisao = num1 // num2
#     print(f"A divisão inteira entre {num1} e {num2} é {divisao}")
# except ValueError:
#     print("Por favor, insira números inteiros válidos.")
# except ZeroDivisionError:
#     print("Não é possível dividir por zero.")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# try:
#     num = float(input("Digite um número: "))
#     quadrado = num ** 2
#     print(f"O quadrado de {num} é {quadrado}")
# except ValueError:
#     print("Por favor, insira um número válido.")


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     soma = num1 + num2
#     print(f"A soma de {num1} e {num2} é igual a {soma}")
# except ValueError:
#     print("Por favor, insira números válidos.")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# def calcula_media(num1, num2):
#     media = (num1 + num2) / 2
#     return media


# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# print(f"A média de {num1} e {num2} é {calcula_media(num1, num2)}")


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# def calcula_potencia(base, expoente):
#     potencia = base ** expoente
#     return potencia


# base = float(input("Digite a base da potencia: "))
# expoente = float(input("Digite o expoente da potencia: "))
# print(f"A potencia de {base} elevado a {expoente} é {calcula_potencia(base, expoente)}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# def converte_celsius_para_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# celsius = float(input("Digite a temperatura em Celsius: "))
# print(f"A temperatura em Fahrenheit é {converte_celsius_para_fahrenheit(celsius)}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math
# def calcula_area_circulo(raio):
#     area_circulo = math.pi * raio ** 2
#     return area_circulo

# raio = float(input("Digite o raio do circulo: "))
# print(f"A área do circulo é {calcula_area_circulo(raio)}")

# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# def converter_maiusculas(texto):
#     return texto.upper()


# texto = input("Digite um texto: ")
# print(converter_maiusculas(texto))

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# def converter_minusculas(texto):
#     return texto.lower()


# texto = input("Digite o seu nome seu nome completo: ")
# print(converter_minusculas(texto))

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# def remove_espacos(texto):
#     return texto.replace(" ", "")


# texto = input("Digite um texto: ")
# print(remove_espacos(texto))

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# def dia_mes_ano(data):
#     return data.split("/")


# data = input("Digite uma data no formato dd/mm/aaaa: ")
# print(f"O dia é {dia_mes_ano(data)[0]}, o mês é {dia_mes_ano(data)[1]} e o ano {dia_mes_ano(data)[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# def concatena_strings(string1, string2):
#     return string1 + string2


# string1 = input("Digite uma palavra ")
# string2 = input("Digite outra palavra ")
# print(concatena_strings(string1, string2))

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
bool1 = input = ("Insira um booleano True ou False ")
bool2 = input = ("Insira outro booleano True ou False")
teste_bool = bool(bool1) AND bool(bool2)

print(f"O resultado da operação lógica entre {bool1} AND {bool2} é {teste_bool}")
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação