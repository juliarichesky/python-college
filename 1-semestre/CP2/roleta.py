# --- 1. CONSTANTES DE PAGAMENTO ---
PAGAMENTO = {
    'Unica': 35,
    'Dupla': 17,
    'Rua': 11,
    'Six': 5,
    'Coluna': 2,
    'Duzia': 2,
    'Par_Impar': 1
}

# --- 2. CONFIGURAÇAO DE JOGADORES E COLEÇÃO DE APOSTAS ---
NUM_JOGADORES = 3

#essa lista vai armazenar as apostas. 
#cada aposta vai ser uma sub-lista: [jogador_id, tipo, valor, numeros_apostados, pagamento_total]
apostas = [] 

print("==============================================")
print("       SIMULADOR DE ROLETA DE CASSINO         ")
print("==============================================")


# --- LOOP PARA COLETAR AS APOSTAS DOS 3 JOGADORES ---
i = 1
while i <= NUM_JOGADORES:
    print(f"\n===== JOGADOR {i} =====")
    
    #menu de apostas
    print("\n--- Tipos de Apostas ---")
    print("1. Unica (Paga 35:1)")
    print("2. Dupla (Paga 17:1)")
    print("3. Rua (Paga 11:1)")
    print("4. Six (Paga 5:1)")
    print("5. Coluna (Paga 2:1)")
    print("6. Duzia (Paga 2:1)")
    print("7. Par ou Impar (Paga 1:1)")
    
    #coleta a escolha
    escolha = int(input("Escolha o tipo de aposta (1-7): "))
    
    #mapeia o numero da escolha para o nome da aposta (usando lista e indice)
    tipos = ['Unica', 'Dupla', 'Rua', 'Six', 'Coluna', 'Duzia', 'Par_Impar']
    
    if 1 <= escolha <= 7:
        tipo_aposta = tipos[escolha - 1]
    else:
        print("Escolha inválida, assumindo 'Unica'.")
        tipo_aposta = 'Unica'

    valor_aposta = float(input("Qual o valor da aposta? R$ "))
    
    numeros_apostados = []


    # --- COLETA DE DADOS ADICIONAIS CONFORME O TIPO DE APOSTA ---
    if tipo_aposta == 'Unica':
        num = int(input("Digite o número (0 a 36) para a aposta Unica: "))
        numeros_apostados = [num]
    
    elif tipo_aposta == 'Dupla':
        num1 = int(input("Digite o primeiro número (0 a 36) para a Dupla: "))
        num2 = int(input("Digite o segundo número (0 a 36) para a Dupla: "))
        numeros_apostados = [num1, num2]
        
    elif tipo_aposta == 'Rua':
        #rua: 3 numeros consecutivos
        print("Rua: Ex: Se digitar 19, aposta em 19, 20, 21.")
        primeiro = int(input("Digite o primeiro número da Rua: "))
        numeros_apostados = [primeiro, primeiro + 1, primeiro + 2]

    elif tipo_aposta == 'Six':
        #six: 6 numeros
        print("Six: Ex: Se digitar 31, aposta em 31 até 36.")
        primeiro = int(input("Digite o primeiro número do Six: "))
        
        #construcao da lista de 6 numeros
        numeros_apostados = [
            primeiro, primeiro + 1, primeiro + 2, 
            primeiro + 3, primeiro + 4, primeiro + 5
        ]

    elif tipo_aposta == 'Coluna':
        #coluna: 12 numeros
        primeiro = int(input("Digite o primeiro número da Coluna (1, 2 ou 3): "))
        
        #construcao da lista da coluna usando loop while
        coluna_num = primeiro
        numeros_apostados = []
        contador = 0
        while contador < 12:
            numeros_apostados = numeros_apostados + [coluna_num] 
            coluna_num = coluna_num + 3
            contador = contador + 1


    elif tipo_aposta == 'Duzia':
        primeiro = int(input("Digite o primeiro número da Duzia (1, 13 ou 25): "))
        
        if primeiro == 1:
            duzia_inicio = 1
        elif primeiro == 13:
            duzia_inicio = 13
        elif primeiro == 25:
            duzia_inicio = 25
        else:
            duzia_inicio = 1
            
        duzia_fim = duzia_inicio + 11 #o ultimo número da duzia
            
        #construcao da lista duzia usando loop while
        duzia_atual = duzia_inicio
        numeros_apostados = []
        while duzia_atual <= duzia_fim:
            numeros_apostados = numeros_apostados + [duzia_atual]
            duzia_atual = duzia_atual + 1


    elif tipo_aposta == 'Par_Impar':
        print("Digite 'p' para Par ou 'i' para Ímpar.")
        escolha_pi = input("Aposta Par ou Ímpar? (p/i): ")
        
        if escolha_pi == 'p':
            numeros_apostados = ['p']
        else:
            numeros_apostados = ['i']


    # --- ARMAZENAMENTO DA APOSTA ---
    # [0: jogador_id
    # 1: tipo
    # 2: valor
    # 3: numeros_apostados
    # 4: pagamento_total]

    aposta_dados = [i, tipo_aposta, valor_aposta, numeros_apostados, 0.0]
    
    #adiciona a lista de aposta_dados para a lista principal 'apostas'
    apostas = apostas + [aposta_dados] 
    
    i = i + 1 #proximo jogador


# --- 3. RESUMO DAS APOSTAS ---
print("\n--- RESUMO DAS APOSTAS ---")

for aposta_item in apostas:
    jogador_id = aposta_item[0]
    tipo = aposta_item[1]
    valor = aposta_item[2]
    
    if tipo == 'Par_Impar':
        escolha_pi = aposta_item[3][0]
        if escolha_pi == 'p':
            nums_info_texto = "Par"
        else:
            nums_info_texto = "Ímpar"
    else:
        nums_info_texto = aposta_item[3] 
    
    print(f"J{jogador_id}: {tipo} - R${valor:.2f} - Números/Tipo: {nums_info_texto}")


# --- 4. SORTEIO DO NUMERO ---
print("\n==============================================")
numero_sorteado = int(input("Digite o número SORTEADO na roleta (0 a 36): "))
        
print(f"\n>>>> O NÚMERO SORTEADO FOI: {numero_sorteado}! <<<<")
print("==============================================")


# --- 5. CALCULAR GANHOS E PERDAS ---
ganho_banca = 0.0

print("\n--- RESULTADO DAS APOSTAS ---")

#loop rodando 3 vezes (pois sabemos que tem 3 jogadores)
j = 0
while j < NUM_JOGADORES:
    aposta = apostas[j] #pega a aposta na posicao 0, 1 e 2
    
    #extrai os dados da lista
    jogador_id = aposta[0]
    tipo_aposta = aposta[1]
    valor_aposta = aposta[2]
    numeros_apostados = aposta[3] 
    
    ganhou = False
    

    # --- LÓGICA DE VERIFICAÇÃO DE VITÓRIA ---
    # 5.1 aposta no 0
    if numero_sorteado == 0:
        #checa se o numero 0 está na lista de apostados (so acontece na aposta unica)
        k = 0
        while k < 37: #checa até um limite grande, para ter certeza que percorre a lista
            if tipo_aposta == 'Unica' and numeros_apostados[k] == 0:
                ganhou = True
            k = k + 1
        
    # 5.2 apostas em numeros (diferente de par/impar)
    elif tipo_aposta != 'Par_Impar':
        #verifica se o numero sorteado esta na lista de numeros apostados
        k = 0
        while k < 37: #checa até 37 (o máximo de numeros possivel)
            if k < len(numeros_apostados):
                if numeros_apostados[k] == numero_sorteado:
                    ganhou = True
                    break
            k = k + 1

    # 5.3 aposta par ou impar (0 é ignorado)
    elif tipo_aposta == 'Par_Impar' and numero_sorteado != 0:
        escolha_pi = numeros_apostados[0] #pega 'p' ou 'i'
        
        numero_par = (numero_sorteado % 2 == 0)
        
        if escolha_pi == 'p' and numero_par:
            ganhou = True
        elif escolha_pi == 'i' and not numero_par:
            ganhou = True


    # --- CALCULO DO PAGAMENTO E AJUSTE DA BANCA ---
    if ganhou:
        multiplicador = PAGAMENTO[tipo_aposta]
        pagamento_total = valor_aposta + (valor_aposta * multiplicador)
        lucro_jogador = pagamento_total - valor_aposta
        
        print(f"JOGADOR {jogador_id} GANHOU! Pagamento total: R${pagamento_total:.2f} (Lucro: R${lucro_jogador:.2f})")
        ganho_banca = ganho_banca - lucro_jogador
        
    else:
        print(f"JOGADOR {jogador_id} PERDEU. Perda: R${valor_aposta:.2f}")
        ganho_banca = ganho_banca + valor_aposta
        
    j = j + 1 #proxima aposta
            

# --- 6. APRESENTAR O GANHO TOTAL DA BANCA ---
print("\n==============================================")
if ganho_banca >= 0:
    print(f"BANCA GANHOU NO TOTAL: R${ganho_banca:.2f}")
else:
    print(f"BANCA PERDEU NO TOTAL: R${abs(ganho_banca):.2f}")
print("==============================================")