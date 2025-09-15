num_a = float(input("Digite um número: "))
op = input("Operador (+-/*): ")
num_b = float(input("Digite um número: "))

if op == '+':
    resultado = num_a + num_b
elif op == '-':
    resultado = num_a - num_b
elif op == '*':
    resultado = num_a * num_b
elif op == '/':
    #teste se o num_b é diferente de zero
    resultado = num_a / num_b
else:
    print("Operador inválido!")

print(f"{num_a} {op} {num_b} = {resultado}")