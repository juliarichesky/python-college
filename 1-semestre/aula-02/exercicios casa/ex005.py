#escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor de π.

#valor constante de π
pi = 3.14

#entrada de dados: leitura do raio pelo usuário
raio = float(input("Digite o valor do raio do círculo: "))

#cálculo da área: A = π × raio²
area = pi * (raio ** 2) #os dois asteríscos significam potenciação.

#cálculo do perímetro (circunferência): P = 2 × π × raio
perimetro = 2 * pi * raio

#saída formatada com duas casas decimais
print(f"A área do círculo é: {area: }")
print(f"O perímetro (circunferência) do círculo é: {perimetro: }")