#Imprimir todos os numeros que aparecem em ambas as listas 

def num_rep(L1, L2):
    
    resultado = []
    
    for i in range(len(L1)):
        for j in range (len(L2)):
            if (L1[i] == L2[j]): #Se os numeros sao iguais, adicionamos a lista de resultado
                if (L1[i] not in resultado): #Impedimos de numeros repetidos em uma mesma lista de se repetirem na lista de resultado
                    resultado.append(L1[i])

    return resultado

#Entrada de teste
L1 = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
L2 = [2, 15, 19, 12, 33, 9, 17, 41, 54, 8]

#Teste
resultado = num_rep(L1, L2)
print(f"{resultado}")
