#Contar o numero de inversoes na lista L

def num_inversoes(L):
    
    cont = 0
    
    for i in range(len(L)): #Elemento que compararemos com todos os outros
        for j in range(i+1, len(L)): #Pula o elemento de comparacao
            if (L[i] > L[j]) and (i < j): #Condicao de inversao
                cont += 1
                
    return cont

#Entrada de teste
lista_teste = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

#Teste
resultado = num_inversoes(lista_teste)
print(f"{resultado}")
