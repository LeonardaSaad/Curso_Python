'''
str = string
'''

#* Utilização recomendada
print("Essa é uma 'string' (str).")
print('Essa é uma "string" (str).')

#* O "\" usado antes do "/' é um caractere de escape, permitindo a reutilização de "/'.
print("Essa é uma \"string\" (str).")
print('Essa é uma \'string\' (str).')


#* \n = quebra de linha
#*  Para evitar que o \n seja executado utiliza "r" antes das aspas

print("Texto \n quebrou a linha")
print(r"Texto \n não quebrou a linha")