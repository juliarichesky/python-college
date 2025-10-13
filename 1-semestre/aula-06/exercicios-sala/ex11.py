import time
#1       1      2     3    5     8     13    21
n = int(input("Qual numero de Fibo vc deseja calcular: "))

ant = 1
atual = 1
while n > 2:
    prox = atual + ant
    ant = atual
    atual = prox
    n = n - 1
    #time.sleep(1) pausa o algoritmo por 1 segundo

print(atual)