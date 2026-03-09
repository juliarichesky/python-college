def particiona_lista(v):
    n = len(v)
    pivo = v[n-1]
    
    # 3. Particionamento (Esquema de Lomuto)
    p = 0 # 'p' será a posição final do pivô
    
    for j in range(0, n - 1):
        # Se o elemento atual for menor que o pivô, ele vai para o lado esquerdo
        if v[j] < pivo:
            v[p], v[j] = v[j], v[p]
            p = p + 1
            
    # 4. Coloca o pivô na sua posição final 'p' (separando os menores dos maiores/iguais)
    v[p], v[n-1] = v[n-1], v[p]
    
    return p

# --- Exemplo de Uso ---
lista = [5, 8, 16, 2, 5, 4, 0, 21, 17, 43, 23, 9]
print(f"Lista original: {lista}")

posicao_pivo = particiona_lista(lista)

print(f"Lista rearranjada: {lista}")
print(f"Posição final do pivô (p): {posicao_pivo}")
print(f"Valor do pivô (v[p]): {lista[posicao_pivo]}")