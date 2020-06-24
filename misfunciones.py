
import random

def promedio(numeros):
        
    if numeros == []:
        print('lista vacia')
    else:
        promedio = sum(numeros) / len(numeros)
           
    return promedio


def lista_aleatoria(inicio, fin, cantidad):
    
    lista = []

    for i in range(cantidad):
        lista.append(random.randint(inicio,fin))

    return lista

def ordenar(numeros):
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados
    
def contar (numeros, numero):
    repeticiones = numeros.count(numero)
    
    return repeticiones 
     
def buscar(numeros, numero):
    lista = []
    
    
    if numero in numeros:
        posicion = numeros.index(numero)
        lista.append(posicion)
        
          
        
    else:
        print('lista vacia')
        
    return lista
