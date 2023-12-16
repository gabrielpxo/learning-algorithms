#Procurar o numero k na lista L. Se ele nao estiver la, retornar o elemento da lista com valor mais proximo de k.

def k_ou_prox(L1, k):

#Variaveis    
    aux = 0
    prox = float('inf')

#Quando o valor e encontrado, ele e retornado
    for i in L1:
        if (k == i):
            aux = 1 
            return i
#Quando o valor nao e encontrado, o numero mais proximo e retornado
    if (aux == 0):
        for i in L1:
            if (prox > ((i-k)**2)):
                prox = ((i-k)**2)
                num_prox = i
    return num_prox

#Teste    
lista = [52, 64, 96, 12, 1, 27]
num = 96
resultado = k_ou_prox(lista, num)
print(resultado)
