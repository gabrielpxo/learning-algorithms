#Verificar se na lista existe algum numero impar que aparece um numero impar de vezes

def impar_impar(L):
    
    #Cria a lista de resultado
    resultado = []
    
    #Assumimos que cada elemento da lista e um numero
    for i in range (len(L)):
        numero = L[i]
        
        #Sendo esse numero impar, contamos sua ocorrencia
        if (numero % 2 != 0):
            cont = ocorrencias(L, numero)

            #Caso o numero ainda nao esteja na lista resultado, adicionamo-lo
            if (cont % 2 != 0 and numero not in resultado):
                resultado = add_numero(resultado, numero)
    
    return resultado

#Contagem de ocorrencias do numero
def ocorrencias(L, numero):
    cont = 0
    for i in range (len(L)):
        if (L[i] == numero):
            cont += 1
   
    return cont

#Adicionando o numero a lista resultado
def add_numero(L, numero):
    
    #A lista atualizada e inicializada com zeros (que indicam os espacos na lista)
    lista_atualizada = [0] * (len(L) + 1) #Entao, multiplicamos esses espacos pelo tamanho da lista resultado mais uma posicao, para caber o novo numero
    for i in range(len(L)): 
        lista_atualizada[i] = L[i] #A nova lista e atualizada contendo os numeros anteriores
    lista_atualizada[-1] = numero #O novo numero e posto no final (-1)
    
    return lista_atualizada
            
#Entrada de teste
lista_teste = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]

#Teste
resultado = impar_impar(lista_teste)
print(f"{resultado}")   
