frase = input("Ingrese una frase: ")
letra = input("Que letra desea buscar: ")

contador = 0

for i in frase:
    if i == letra:
        contador = contador+1

print("La letra",letra,"aparece",contador,"veces en la frase: ",frase)
