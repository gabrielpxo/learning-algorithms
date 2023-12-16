#Encontrar os dois elementos da lista L que possuem a menor diferenca entre si em valor absoluto

def menor_dif(L):
    
    dif = float('inf') #A diferenca inicial e a maior possivel
    menor = [] #Aqui temos a lista que retornara os numeros com menor diferenca
    
    for i in range(len(L)):
        
        for j in range(len(L)):
            
            #A dif absoluta deve ser menor que a dif atual e os elementos devem ser diferentes
            if (abs(L[i] - L[j]) < dif) and (i != j): 
                dif = abs(L[i] - L[j]) #A dif atual passa a ser a menor
                menor = [L[i], L[j]] #A lista de resultado recebe os dois elementos
    
    return menor

#Entrada de teste
lista_teste = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

#Teste
resultado = menor_dif(lista_teste)
print(f"{resultado}")
