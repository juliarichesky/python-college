#pegue seu CPF e faça o cálculo do dígito verificador usando o algoritmo apresentado. use lápis e papel para esse propósito.

#CPF ABC.DEF.GHI-JK
#CPF: 123.456.789-10

#DIGITO VERIFICADOR J
print("Estamos verificando os dígitos do seu CPF: ")
soma_j = 10*1 + 9*2 + 8*3 + 7*4 + 6*5 + 5*6 + 4*7 + 3*8 + 2*9

resto_j = soma_j % 11

if resto_j < 2:
    j = 0
else:
    j = 11 - resto_j
print(f"Seu número verificador J é: {resto_j}")

#DIGITO VERIFICADOR K
soma_k = 11*1 + 10*2 + 9*3 + 8*4 + 7*5 + 6*6 + 5*7 + 4*8 + 3*9 + 2*1

resto_k = soma_k % 11

if resto_k < 2:
    k = 0
else:
    k = 11 - resto_k
print(f"Seu número verificador K é: {resto_k}")