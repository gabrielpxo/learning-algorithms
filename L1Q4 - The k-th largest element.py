#Encontrar o k-esimo maior elemento da lista L

def k_maior_elemento (L1, k):
    
    #Basta repetir o procedimento de colocar o maior numero no final da lista k vezes
    cont = 0
    while cont != k:
        
        n = len(L1)
        maior = L1[0]
        maior_pos = 0
        
        for i in range (1, n):
            if maior < L1[i]:
                maior = L1[i]
                maior_pos = i
        
        aux = L1[maior_pos]
        L1[maior_pos] = L1[n-1]
        L1[n-1] = aux
        
        cont += 1
        
        return L1[n-k]

import random
lista_teste = []
for _ in range(10):
    numero_aleatorio = random.randint(1,100)
    lista_teste.append(numero_aleatorio)
print(f"Lista: {lista_teste}")

entrada_k = input("Escolha um k de 1 a 10: ")
k_escolhido = int(entrada_k)

resultado = k_maior_elemento (lista_teste, k_escolhido)
print(f"O k maior elemento e: {resultado}")
        
