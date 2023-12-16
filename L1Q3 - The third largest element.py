#Encontrar o terceiro maior elemento da lista L

def terc_maior_impar(L1):
    
#Inicializa variaveis
    maior = -1
    maior_pos = float('-inf')
    seg_maior = -1
    seg_maior_pos = float('inf')
    terc_maior = -1

#Passo II: encontra o maior
    for i in range(len(L1)):
        if (L1[i] > maior):
            maior = L1[i]
            maior_pos = i
            
#Passo III: coloca o maior na ultima posicao
    L1[maior_pos], L1[-1] = L1[-1], L1[maior_pos]
    
#Passo IV: busca o maior valor de L[0] a L[n-1]
    for i in range(len(L1)-1):
        if (L1[i] > seg_maior):
           seg_maior = L1[i]
           seg_maior_pos = i
    
#Passo V: coloca o segundo maior numero na penultima posicao    
    L1[seg_maior_pos], L1[-2] = L1[-2], L1[seg_maior_pos]
    
#Passo VI: busca o maior valor de L[0] a L[n-2]    
    for i in range(len(L1)-2):
        if (L1[i] > terc_maior):
           terc_maior = L1[i]
    
    return terc_maior

#Cria uma lista aleatoria
import random
lista_teste = []
for _ in range(10):
    numero_aleatorio = random.randint(1,100)
    lista_teste.append(numero_aleatorio)
print(f"Lista: {lista_teste}")

#Teste
resultado = terc_maior_impar(lista_teste)
print(f"Seu terceiro maior numero e: {resultado}")
