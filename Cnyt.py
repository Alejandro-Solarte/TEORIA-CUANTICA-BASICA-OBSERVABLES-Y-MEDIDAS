from calculadora_matrices_vectores import *
import numpy as np
import math
def valor_esperado (m1,v):
    '''Recibe una matriz hermitania y vector donde calcula el vector que se espera'''
    if matriz_hermetica(m1):
        mat = []
        mult = []
        for i in range(len(m1)):
            suma = (0,0)
            for j in range(len(m1[0])):
                m = pro_com(m1[i][j],v[j])
                suma = sum_com(suma,m)
            mult.append(suma)
        inter = producto_interno(mult,v)
        return inter

def varianza (m,v):
    '''Esta función recibe una matriz hermitiana y un vector a lo cual calcula la varianza'''
    valor = valor_esperado(m1,v)
    ident = []
    for i in range(len(m)):
        fil = []
        for j in range(len(m[0])):
            if j == i:
                fil.append((1,0))
            else:
                fil.append((0,0))
        ident.append(fila)
    multiplicacion = multiplicacion_escalar_matrizimg(valor[0],ident)
    delta = rest_com(m,multiplicacion)
    multmat = pro_com(delta,delta)
    mult = []
    for i in range(len(multmat)):
            suma = (0,0)
            for j in range(len(multmat[0])):
                m = pro_com(multmat[i][j],v[j])
                suma = sum_com(suma,m)
            mult.append(suma)
    producto = producto_interno(mult,v)
    return producto

def valores__vectores_propios(mat):
    '''Esta función recibe una matriz y devuelve vectores y valores usando la libreria numpy'''
    valores,vectores = np.linalg.eig(mat)
    return valores,vectores

def probabilidad_sistema_eigenvalue(mat,sistem):
    '''Calcula la probablidad de un sistema tansite y da como resultado un arreglo con probabilidades'''
    valores,vector = valores__vectores_propios(mat)
    probabilidades = []
    for i in range(len(vector)):
        proba = abs(np.dot(sistem,vector[i]))
        probabilidades.append(proba)
    return probabilidades
