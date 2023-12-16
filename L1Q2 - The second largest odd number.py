#Encontrar o segundo maior numero impar armazenado na lista L, se ele existir.

def seg_maior_impar(L1):
    
#Inicializa variaveis
    maior = -1
    maior_pos = float('-inf')
    seg_maior = -1

#Passo II: encontra o maior impar
    for i in range(len(L1)):
        if (L1[i] % 2 != 0) and (L1[i] > maior):
            maior = L1[i]
            maior_pos = i
            
#Passo III: coloca o maior impar na ultima posicao
    L1[maior_pos], L1[-1] = L1[-1], L1[maior_pos]
    
#Passo IV: busca o maior valor impar de L[0] a L[n-1]
    for i in range(len(L1)-1):
        if (L1[i] % 2 != 0) and (L1[i] > seg_maior):
           seg_maior = L1[i]
                
    return seg_maior

#Cria uma lista aleatoria
import random
lista_teste = []
for _ in range(10):
    numero_aleatorio = random.randint(1,100)
    lista_teste.append(numero_aleatorio)
print(f"Lista: {lista_teste}")

#Teste
resultado = seg_maior_impar(lista_teste)
print(f"Seu segundo maior numero impar e: {resultado}")
