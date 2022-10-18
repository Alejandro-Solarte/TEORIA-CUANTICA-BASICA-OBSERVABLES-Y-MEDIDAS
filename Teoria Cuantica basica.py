from calculadora_matrices_vectores import *
from calculadora_numeros_complejos import *
import math
def ver_normalizado(v):
    '''Recibe un arreglo donde la funcion se calcula la norma, devuelve true si el resultado es True'''
    norma = norma_vector(v1)
    if norma == 1:
        return True
    else:
        return False
def normalizar (v):
    '''Cuando el resultado de la norma es diferente a 1, se multiplica el arreglo por 1/norma'''
    div = 1/norma_vector(v1)
    if ver_normalizado(v):
        return v
    else:
        vector = multiplicacion_escalar_matriz(n1,m)
        return vector
    
def probabilidad (v,x):
    '''Recibe posicion y vector, devuelve el valor de la probabilidad'''
    ve = normalizar(v)
    vect = NormVect(ve)
    pos = ModComplex(v[x])
    proba = (pos**2)/(vect**2)
    resultado = proba * 100
    return resultado

def amplitud(v1,v2):
    '''recibe dos vectores donde se calcula cual es la amplitud de uno a otro'''
    v1_norm = normalizar(v1)
    v2_norm = normalizar(v2)
    resultado = ProductInterVect(v2_norm,v1_norm)
    return resultado
    