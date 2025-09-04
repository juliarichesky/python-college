auxiliar = input("Digite a base: ")
base = float(auxiliar)

auxiliar = input("Digite a altura")
altura = float(auxiliar)

area = base * altura / 2

#alguns exemplos de print
print("A área vale: " + str(area)) #concatenar 2 strings, se fosse número ia somar
print("A área vale: ", area, "cm^2") #-> vários parâmetros para o print
print(f"A área vale: {area}") #-> f-string: importante aprender!