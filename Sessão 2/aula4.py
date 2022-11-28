"""
Tipos de daos
str - string - texto                    "Assim" 'Assim'
int - inteiro                           123456, 0, -10, -20
float - real/ponto flutuante            10.50, 1.5, 50.90
bool - booleano/lógico                  true/false
"""

#*  type() mostra a classe do que está dentro dele.
print("Luiz", type("Luiz"))
print("123", type("123"))
print(123, type(123))
print(10.50, type(10.50))
print(10 == 10, type(10 == 10))         # Dez é igual a dez. verdade
print("l" == "L", type("l" == "L"))     # l é igual a L. falso


#* Conversão de tipo

# Booleano
print(bool(""))
print(bool(0))
print("Luiz", type("Luiz"), bool("Luiz"))

# String
print(10, type(10), type(str(10)))

# Integer
print("50", type("50"), type(int("50")))

# Float
print("6.5", type("6.5"), type(float("6.5")))


#*  +
print(10 + 10)          # soma
print("10" + "10")      # concatenação


#! Exercício
    #*  Print seu nome(str), idade(int), altura(float) e cheque se você é maior de idade.

print("Nome:", "Leonarda Saad S.", type("Leonarda Saad S."))
print("Idade:", 18, type(18))
print("Altura:", 1.65, type(1.65))
print("Maior de idade?", 18 >= 18, type(18 >= 18))
