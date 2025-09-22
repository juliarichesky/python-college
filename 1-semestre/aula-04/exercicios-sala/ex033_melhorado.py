num_a = float(input("Digite um número: "))
op = input("Operador (+-/*): ")
num_b = float(input("Digite um número: "))
fez_conta = True #DRY

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
    quit() # -> encerrar o programa, não executar mais nada
    fez_conta = False #precisa desse porque é o contrário
if fez_conta: #== True: não é necessário usar
    print(f"{num_a} {op} {num_b} = {resultado:.3f}")