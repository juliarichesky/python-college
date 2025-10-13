import random
import datetime

senha = 127  #só para nao mostrar 1 como primeira senha
opcao = 'a'  #qualquer valor menos o 6

while opcao != 6:
    print('''Pronto atendimento --- Hospital Cura Certa\n
    \t1) retirada de senha\n\t2) triagem\n\t3) cadastra paciente\n\t4) consulta médica
    \t5) atendimento\n\t6) sair''')

    opcao = int(input("Opção: "))
    if opcao == 1:
        tempo = int(random.random() * 60)
        print(f"Sua senha é {senha} e o tempo estimado de espera é {tempo} min")
        senha = senha + 1

    elif opcao == 2:
        sintomas = input("Sintomas: ")
        temperatura = float(input("Temperatura: "))
        pressao = input("Pressão: ")
        peso = int(input("Peso: "))
        alergias = input("Alergias: ")
        aux = input("Prioridade (S/N): ")
        prioridade = False
        if aux == 's' or aux == 'S':
            prioridade = True

    elif opcao == 3:
        nome = input("Nome completo: ")
        tel = input("Telefone: ")
        end = input("Endereço: ")
        cpf = int(input("CPF: "))
        convenio = input("Convênio: ")
        print(f"Data e hora do atendimento: {datetime.datetime.now()}")
    elif opcao == 4 or opcao == 5:
        print("Consulta ou atendimento de medicaçao")
    elif opcao == 6:
        print("Espero que tenha sido bem atendido. Volte sempre!")
    else:
        print("Opção inválida. Escolha corretamente.")