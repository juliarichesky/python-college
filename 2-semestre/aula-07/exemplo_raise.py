import math
def raiz_quadrada(numero: float) -> float:
    if numero < 0:
        raise Exception("Função raiz_quadrada não aceita negativos")
    return math.sqrt(numero)


valor = float(input("Valor: "))
try:
    result = raiz_quadrada(valor)
except Exception as erro:
    print("usuario digitou um valor invalido (negativo?)!")
    print(erro)
else:
    print(result)
