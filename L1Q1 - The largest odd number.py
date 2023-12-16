#Encontrar o maior numero impar armazenado na lista L, se houver algum.

def maior_impar(L1):
    
    maior = -1 #Retorna -1, caso nao haja impares.
    
    for i in L1: #Para cada elemento de L1,
        if (i%2 != 0) and (i > maior): #se ele for impar e maior que o "maior",
             maior = i #a variavel atualiza.
                
    return maior

#Cria uma lista aleatoria
import random
lista_teste = []
for _ in range(10):
    numero_aleatorio = random.randint(1,100)
    lista_teste.append(numero_aleatorio)
print(f"Lista: {lista_teste}")

#Teste
resultado = maior_impar(lista_teste)
print(f"Seu maior numero impar e: {resultado}")
