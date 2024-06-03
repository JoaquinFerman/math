
#######################################################################################################

def mult_matrix(matriz1:list, matriz2:list) -> list:
    # Transpondo la matriz a multiplicar
    matriz2 = transpond(matriz2)

    # Creo una matriz nueva vacia con las dimenciones correspondientes
    matriz_final = [[0]*len(matriz2) for _ in range(len(matriz1))]
    # Por cada fila
    for i in range(len(matriz1)):
        # Por cada columna
        for j in range(len(matriz1)):
            # Por cada parte de la "suma"
            for k in range(len(matriz1[0])):
                matriz_final[i][j] += matriz1[i][k] * matriz2[j][k]
    # [[a, b]    [[g, h]    [[ag+bh, ai+bj, ak+bl]
    #  [c, d]  x  [i, j]  =  [cg+dh, ci+dj, ck+dl]
    #  [e, f]]    [k, l]]    [eg+fh, ei+fj, ek+fl]]
    return(matriz_final)

def transpond(matriz:list) -> list:
    # Creo una matriz en blanco con las dimenciones invertidas
    newmatriz = [[0]*len(matriz) for _ in range(len(matriz[0]))]
    # Por cada fila
    for i in range(len(matriz)):
        # Por cada columna
        for j in range(len(matriz[0])):
            # Reemplazo el valor vacio de la matriz nueva en la posicion opuesta por el de la matriz vieja
            newmatriz[j][i] = matriz[i][j]

    return newmatriz

#######################################################################################################

m1 = [[1, 2], [3, 4], [1, 2]]
m2 = [[1, 2, 1], [3, 4, 2]]

print(mult_matrix(m1, m2))