"""
Introdução à formatação de string
"""

nome = "Carlos"
idade = 29
altura = 1.80
peso = 70
e_maior = idade > 18
imc = peso / (altura**2)

print(f"{nome} tem {idade} anos e seu imc é {imc:.2f}")
print("{0} tem {1} anos de idade e seu imc é {2}.".format(nome,idade,imc))
print("{2} {0} tem {1} anos de idade e seu imc é {2}.".format(nome,idade,imc))
print("{n} tem {i} anos de idade e seu imc é {im}.".format(n=nome,i=idade,im=imc))


#* (f"") permite que utilizemos com mais facilidade variáveis dentro das aspas.
#* :.<número de casas decimais>f  ao colocarmos isso depois do nome de uma variável, limita o número de casas decimais.
#* .format(<variáveis>) Utilizamos essa função depois das aspas.