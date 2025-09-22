salario = float(input("Salário: "))
sal_min = 1518.00
qtd = salario / sal_min

if qtd > 10:
    print("Puxa vida, você ganha bem!")
    print("......")

print(f"Seu salário de {salario} equivale a {qtd} de salários mínimos")