dia_semana = input("Informe o dia da semana: ")

match dia_semana:
    case 'segunda':
        print("Strogonoff")
    case 'terca':
        print("Lasanha 4 Queijos")
    case 'quarta':
        print("Feijoada")
    case 'quinta':
        print("Macarrão a Bolonhesa")
    case 'sexta':
        print("Peixe Empanado")
    case 'sabado':
        print("Pizza")
    case _:
        print("Almoço da mãe")