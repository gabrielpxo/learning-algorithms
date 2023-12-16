#Verificar se existem dois elementos na lista L tal que um deles e o dobro do outro
#Obs.: Isso implica que um será metade do outro

def dobro(L):
    
    for i in range(len(L)): #Assumimos que cada elemento da lista e um numero
        numero = L[i]
        
        for j in range(len(L)): #Comparamo-lo com todos os outros
            if (L[j] == (numero * 2) or L[j] == (numero / 2)): #Se o numero for o dobro ou metade de outro,
                print(f"{numero}, {L[j]}") #Imprimimos os dois e retornamos verdadeiro
                return True

    return False #Se nao há algum numero assim, retornamos falso

#Entrada de teste
lista_teste = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

#Teste
resultado = dobro(lista_teste)
print(f"{resultado}")
