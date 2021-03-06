#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import random
import math


def ej1():
    # Ejercicios con funciones del sistema
    numeros = [2, 4, 6, 8, 10, 12]

    prom = promedio(numeros)

    print('el promedio es',prom)

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle
    https://docs.python.org/3.7/library/functions.html

    La función debe retornar el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado
    '''
    

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



def ej2():
    # Ejercicios con modulos del sistema
    inicio = 0
    fin = 10
    
    lista_aleatoria2 = lista_aleatoria(0, 10, 5)
    
    print(lista_aleatoria2)

      
    numero_1 = random.choice (lista_aleatoria2)  
    numero_2 = random.choice (lista_aleatoria2)

    print ('los numeros aleatorios son:',numero_1,'y',numero_2) 

    
    raiz_cuadrada_1 = math.sqrt(numero_1)
    raiz_cuadrada_2 = math.sqrt(numero_2)
    
    print('la raiz cuadrada de n1 es:',raiz_cuadrada_1,'y la del n2 es:',raiz_cuadrada_2)

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    
     
    


    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.
    def lista_aleatoria (inicio, fin, cantidad)

    Dicha función debe retornar la lista de elementos random generados.
    '''


    

    # numeros = lista_aleatoria (inicio, fin, cantidad)

    # Imprima en pantalla la lista de elementos generados
    # print(....)

    # Utilice el método random.choice para obtener 2 numeros
    # de la lista de elementos generados
    # numero_1 = random.choice(...)
    # numero_2 = random.choice(...)

    
      
      

    # Importar en este programa/documento el modulo "math"
    # Calcular la raiz cuadrada (square root) de esos
    # dos numeros obtenidos utilizando el método del
    # módulo "math" que crea correspondiente
    # Documentación oficial de math
    # https://docs.python.org/3.7/library/math.html
    # NOTA: Puede buscar en el medio que prefiera la info
    # solicitada

    # raiz_cuadrada_1 = ....
    # raiz_cuadrada_2 = ....


    
def ej3():
    numeros = [2, 6, 4, 7, 17, 12]

    

    lista_ordenada = ordenar(numeros)
    print('la lista ordenada es',lista_ordenada)

def ordenar(numeros):
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados
    
    
    


    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.

    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python
    La función no hace falta que retorne la lista ordenada,
    ya que al tratarce de una lista se pasa como referencia
    a la función (es decir que las modificaciones realizadas
    en la función afectan a la variable pasada como argumento)

    '''


    



def ej4():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado 
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''
    
    lista_numeros = lista_aleatoria(0, 10, 5)

    cantidad_uno = contar(lista_numeros, 1)
    print('el numero 1 se repite:',cantidad_uno)

def contar (numeros, numero):
    repeticiones = numeros.count(numero)
    
    return repeticiones 
     
     
    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)

def ej5():
    # Ejercicios de listas y métodos
 

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "buscar",
    que genere una lista con los índice de las posiciones
    en donde se encuentra dicho elemento en la lista.
    Si el elemento en la lista no existe, la función
    debe retornar una lista vacia.
    Para encontrar los índices del elemento en la lista
    puede usar el método "index" o bucles.
    Recuerde que el elemento puede repetirse más de una
    vez en la lista.
    '''
    lista_numeros = lista_aleatoria(1, 9, 5)
    num_usuario = int(input('ingrese numero:\n'))
    lista_posicion = buscar(lista_numeros, num_usuario)
    print(lista_posicion)

def buscar(numeros, numero):
    lista = []
    
    
    if numero in numeros:
        posicion = numeros.index(numero)
        lista.append(posicion)
        
          
        
    else:
        print('lista vacia')
        
    return lista

    #como generar una lista con varias posiciones de un numero que se repite.

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
