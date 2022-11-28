"""
Input
    * Ela permite a entrada de dados
"""


nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_atual = 2022
ano_nascimento = ano_atual - int(idade)

print(nome,idade,ano_nascimento)