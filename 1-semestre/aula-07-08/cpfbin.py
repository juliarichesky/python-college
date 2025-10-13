cpf = int(input("Informe o CPF sem fmt: "))

digitos = cpf % 100
cpf = cpf // 100

parte3 = cpf % 1000
cpf = cpf // 1000

parte2 = cpf % 1000
cpf = cpf // 1000

cpf_fmt = f"{cpf}.{parte2}.{parte3}-{digitos}"
print(cpf_fmt)