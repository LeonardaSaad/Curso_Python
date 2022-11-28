"""
isnumeric, isdigit, isdecimal
    * Checam se o valor é um número e se ele é positivo, retornando True/False
    * Números de ponto flutuante não contam
"""
"""
num1 = input('Digite um número: ')

print(f'{num1} é numerico?', num1.isnumeric())
print(f'{num1} é um digito?', num1.isdigit())
print(f'{num1} é decimal?', num1.isdecimal())
"""

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1+num2)
else:
    print("Não pude converter os números para realizar a conta.")