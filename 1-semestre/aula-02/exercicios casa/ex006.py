#sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o dígito das dezenas e o dígito das unidades desse número. dica: usando papel e lápis faça a divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão.

numero = int(input("Digite um número entre 0 e 99: "))


#obtém o dígito das dezenas
dezenas = numero // 10

#obtém o dígito das unidades
unidades = numero % 10

print(f"Dígito das dezenas: {dezenas}")
print(f"Dígito das unidades: {unidades}")