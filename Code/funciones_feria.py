# -*- coding: utf-8 -*-
import math as math
import random as rand

# Juego 1: Buscar la bolita

def buscar_bolita(posicion_inicial: int, posicion_apuesta: int)->bool:
    """ Esta función ubica la bolita en la posición inicial indicada, hace 3 intercambios aleatorios y
        finalmente informa si la bolita quedó en la posición por la que apostó el jugador.
    Parámetros:
        posicion_inicial (int): es el número del vaso en el que va a quedar la bolita inicialmente (1, 2 o 3)
        posicion_apuesta (int): es el número del vaso en el que el jugador supone que va a quedar la bolita (1, 2 o 3)    
    Retorno:
        Retorna True si la bolita quedó en la posición apostada y False en caso contrario.
    """
    
    #TODO:completar la función para simular los 3 movimientos aleatorios entre los vasos
    #Use las variables booleanas vaso1, vaso2 y vaso3 para indicar respectivamente si el vaso 1 contiene la bolita (True) o
    #no la contiene (False), si el vaso 2 contiene la bolita (True) o no la contiene (False) y si el vaso 3 contiene 
    #la bolita (True) o no la contiene (False)

    mov_1=(rand.randint(1,3))
    mov_2=(rand.randint(1,3))
    mov_3=(rand.randint(1,3))

    #TODO: Inicialización de las variables vaso1, vaso2 y vaso3 de acuerdo a la posición inicial de la bolita dada por el usuario

    vaso_1=False
    vaso_2 = False
    vaso_3 = False

    if posicion_inicial == 1:
        vaso_1 = not vaso_1

    elif posicion_inicial == 2:
        vaso_2 = not vaso_2

    else:
        vaso_3 = not vaso_3

    #TODO simular el primer intercambio aleatorio de vasos

    if mov_1==1:
        vaso_1=not vaso_1
        vaso_2 = not vaso_2

    elif mov_1==2:
        vaso_2 = not vaso_2
        vaso_3 = not vaso_3

    else:
        vaso_1 = not vaso_1
        vaso_3 = not vaso_3

       
    #TODO: completar los otros posibles movimientos

    #TODO: simular el segundo y tercer intercambio aleatorio

    #Segundo movimiento

    if mov_2==1:
        vaso_1=not vaso_1
        vaso_2 = not vaso_2

    elif mov_2==2:
        vaso_2 = not vaso_2
        vaso_3 = not vaso_3

    else:
        vaso_1 = not vaso_1
        vaso_3 = not vaso_3



    #TODO Llamar a la función es_ganador para determinar si el jugador ganó o perdió y dejar el resultado en la variable gano
    gano = False

    return gano


def es_ganador(posicion_apuesta, vaso1: bool, vaso2: bool, vaso3: bool)->bool:
    """ Esta función indica si el jugador ganó dependiendo de su apuesta y dependiendo del contenido de los vasos.
    Parámetros:
        posicion_apuesta (int): es la posición en la que el jugador supone que va a estar la bolita (1, 2 o 3)
        vaso1 (bool): es True si la bolita se encuentra en el vaso 1 y False de lo contrario.
        vaso2 (bool): es True si la bolita se encuentra en el vaso 2 y False de lo contrario.
        vaso3 (bool): es True si la bolita se encuentra en el vaso 3 y False de lo contrario.
    Retorno:
        Retorna True si el jugador ganó su apuesta y False en caso contrario.
    """
    # TODO: completar la implementación de la función. 
	# Cuando haya completado la función con su verdadero valor de retorno, borre la siguiente línea.
    return False


# Juego 2: Tiro al blanco

def tiro_al_blanco(velocidad_inicial: float, angulo_alfa: float, angulo_beta: float)->int:
    """ Esta función calcula los puntos obtenidos por un jugador dados los datos de su lanzamiento.
    La mesa se encuentra ubicada a 7 metros del lugar de lanzamiento.
    El blanco tiene 4 zonas de 10, 20, 30 y 40 cms de diámetro, que dan 50, 20, 10 y 5 puntos respectivamente.
    Parámetros:
        velocidad_inicial (float): la velocidad inicial en kilómetros/horaa la que sale la bola lanzada.
        angulo_alfa (float): el ángulo en grados al que sale la bola con respecto a la horizontal.
        angulo_beta (float): el ángulo en grados al que sale la bola con respecto a la línea recta entre el punto de lanzamiento y el centro del blanco.
    Retorno:
        La cantidad de puntos obtenidos por el jugador
    """
    # TODO: completar la implementación de la función. 
	# Cuando haya completado la función con su verdadero valor de retorno, borre la siguiente línea.
    return 1


def calcular_distancia_tiro(velocidad_inicial: float, angulo_alfa: float, angulo_beta: float)->float:
    """ Calcula la distancia horizontal recorrida por la bola desde el lanzamiento hasta que caiga sobre la mesa.
    Parámetros:
        velocidad_inicial (float): la velocidad inicial en metros/segundo a la que sale la bola lanzada.
        angulo_alfa (float): el ángulo en grados al que sale la bola con respecto a la horizontal.
        angulo_beta (float): el ángulo en grados al que sale la bola con respecto a la línea recta entre el punto de lanzamiento y el centro del blanco.
    Retorno:
        La distancia en metros del lanzamiento
    """
    # TODO: completar la implementación de la función. 
	# Cuando haya completado la función con su verdadero valor de retorno, borre la siguiente línea.
    return 1


def calcular_tiempo_tiro(velocidad_vertical_inicial: float)->float:
    """ Calcula el tiempo que le toma a la bola caer sobre la mesa.
    Parámetros:
        velocidad_vertical_inicial (float): la componente vertical de la velocidad inicial en metros/segundo 
        a la que sale la bola lanzada.
    Retorno:
        La cantidad de segundos que le toma a la bola llegar a la mesa
    """
    # TODO: completar la implementación de la función. 
	# Cuando haya completado la función con su verdadero valor de retorno, borre la siguiente línea.
    return 1


def calcular_x_tiro(distancia_tiro: float, distancia_mesa: int, angulo_beta: float)->float:
    """ Calcula la coordenada X del lugar donde cayó la bola, teniendo el centro de la mesa como la coordenada 0,0.
    Parámetros:
        distancia_tiro (float): la distancia en metros recorrida por la bola durante el lanzamiento
        distancia_mesa (float): la distancia en metros entre el lugar del lanzamiento y el centro de la mesa
        angulo_beta (float): el ángulo en grados al que sale la bola con respecto a la línea recta entre el punto de lanzamiento y el centro del blanco.        
    Retorno:
        La coordenada x del lanzamiento, en centímetros
    """
    # TODO: completar la implementación de la función. 
	# Cuando haya completado la función con su verdadero valor de retorno, borre la siguiente línea.
    return 1


def calcular_y_tiro(distancia_tiro: float, distancia_mesa: int, angulo_beta: float)->float:
    """ Calcula la coordenada Y del lugar donde cayó la bola, teniendo el centro de la mesa como la coordenada 0,0.
    Parámetros:
        distancia_tiro (float): la distancia en metros recorrida por la bola durante el lanzamiento
        distancia_mesa (float): la distancia en metros entre el lugar del lanzamiento y el centro de la mesa
        angulo_beta (float): el ángulo en grados al que sale la bola con respecto a la línea recta entre el punto de lanzamiento y el centro del blanco.        
    Retorno:
        La coordenada y del lanzamiento, en centímetros
    """
    # TODO: completar la implementación de la función. 
	# Cuando haya completado la función con su verdadero valor de retorno, borre la siguiente línea.
    return 1


def calcular_puntos(x: float, y: float, radio1: int, radio2: int, radio3: int, radio4: int)->int:
    """ Calcula la cantidad de puntos que ganó el usuario dada la posición donde cayó la bola.
    La coordenada 0,0 corresponde al centro de la mesa.
    Parametros:
        x (float): la coordenada x del lanzamiento, en centímetros
        y (float): la coordenada y del lanzamiento, en centímetros
        radio1 (int): el radio en centímetros de la zona 1 de la mesa (la zona más interna) que da 50 puntos
        radio2 (int): el radio en centímetros de la zona 2 de la mesa que da 20 puntos
        radio3 (int): el radio en centímetros de la zona 3 de la mesa que da 10 puntos
        radio4 (int): el radio en centímetros de la zona 4 de la mesa (la zona más externa) que da 5 puntos
    Retorno:
        La cantidad de puntos obtenidos por el jugador
    """
    # TODO: completar la implementación de la función. 
	# Cuando haya completado la función con su verdadero valor de retorno, borre la siguiente línea.
    return 1

