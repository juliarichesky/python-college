#escreva um algoritmo que recebe um número x e y e imprime x^y. lembre-se que ∗∗ representa a potência entre dois números em python.

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

#calcula x elevado a y
resultado = x ** y

#imprime o resultado
print(f"{x} elevado a {y} é {resultado}")