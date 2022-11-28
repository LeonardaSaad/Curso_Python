
#! Print
    # Função, que exibe/retorna string, número ou variável.

    # Se os 2 textos forem unidos por ",", automaricamente haverá uma espaço entre eles;
    # Se o 2 textos forem unidos por "+", não haverá espaço entre eles;


print("Texto", "outro texto" + "mais um")       # String
print(123)                                      # Number

# --------------------------------------------------------------

#! sep="<separador>"
    # Separa todos os textos por um separador


print("A", "aa", sep="-")

# --------------------------------------------------------------

#! end=""
    # Coloca qualquer coisa depois dos dados já inseridos e quebra linha


print("A", "aa", sep="-", end="=====")
print("B", "bb", sep="-")

# --------------------------------------------------------------

#! Exercício:
    # Print de "824.176.070-18" usando sep e end.

print(824,176, "070", sep=".", end="-")
print(18)
