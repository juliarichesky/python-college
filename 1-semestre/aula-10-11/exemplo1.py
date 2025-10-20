disciplinas = ['CTP', 'DDD', 'Database', 'Front-end', 'IA & Chatbot', 'Software engineering']

tamanho = len(disciplinas)
print(f"Tamanho da lista: {tamanho}")

#for-each: percorre todos os elementos da minha lista sem exceção
#do primeiro até o último
for disc in disciplinas:
    print(disc)

disciplinas.append("Formação social")

print("=" * 40)

k = len(disciplinas) - 1 #posicionando k no último índice da lista disciplinas
while k >= 0:
    print(disciplinas[k])
    k = k - 1
