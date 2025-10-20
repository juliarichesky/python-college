#considere um corredor com mil portas, numeradas de 1 a 1000, que se encontram todas fechadas. por esse corredor passarão mil pessoas, que modificarão o estado das portas cujo número seja múltiplo do seu número de passagem: a pessoa com o número 3 modificará o estado (fechará se estiverem abertas ou abrirá se estiverem fechadas) das portas $n^{0}$ 3, 6, 9, 12, ... e a pessoa com o número 7 fará o mesmo às portas 7, 14, 21, etc.

#construa um programa que permita saber quantas são e quais são as portas abertas após a passagem
# da milésima pessoa.

#dica: use uma lista onde você armazena valores true ou false com 1001 posições para representar as portas.
#dica, crie uma função para ajudar a resolver o problema.