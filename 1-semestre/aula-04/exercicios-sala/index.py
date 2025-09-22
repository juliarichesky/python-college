#informações dos slides


#entrada de dados
placarA = int(input("Gols do time A:"))
placarB = int(input("Gols do time B:"))

#decidindo resultado
if placarA == placarB :
    print ("Empate ")
else :
    if placarA > placarB :
        print ("Time A ")
    else :
        print ("Vencedor Time B")

print ("Fim do programa ")


#SOLUÇÃO COM ELIF

#entrada de dados
placarA = int (input ("Gols do time A:"))
placarB = int (input ("Gols do time B:"))

#decidindo resultado
if placarA == placarB :
    print ("Empate ")
elif placarA > placarB :
    print ("Time A")
else:
    print ("Vencedor Time B")

print ("Fim do programa")

#nao há limite para o comando elif, mas ele só pode aparecer após uma instrução if