frutas = ["uva", "kiwi", "maca", "caqui"]
print(frutas[2]) #aqui vai imprimir maca
frutas[2] = "laranja"
print(frutas) #aqui agora é laranja, nao maca

remove = frutas.pop(1)
print(frutas)

del frutas[0]
print(frutas)

frutas[2] = "banana"