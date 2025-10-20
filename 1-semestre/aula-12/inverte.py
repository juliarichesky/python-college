#escreva uma função que inverte o conteúdo da lista. você não deve chamar nenhuma função/método do python e nem usar índices negativos.

#além disso, sua função deverá inverter o conteúdo na própria lista, ou seja, nenhuma lista auxiliar deverá ser criada.

#(lista: list) indica o parâmetro daquela função. O ": list" serve para deixar mais claro do que aquilo se trata.
def inverte(lista: list) -> None:
    ini = 0
    fim = len(lista) - 1

        #julia #ilda
    while ini < fim:
        aux = lista[ini]
        lista[ini] = lista[fim]
        lista[fim] = ini + 1
        fim = fim - 1

    aux = lista[ini]
    lista[ini] = lista[fim]
    lista[fim] = aux
    ini = ini + 1
    fim = fim - 1

lst = [4, 82, -98, 0, 34, 6, -10, -16]
inverte(lst)
print(lst)

#nome = "Silva"
#sobrenome = "Marcos"

#aux = nome
#nome = sobrenome
#sobrenome = aux