from math import sqrt
from admin_particula import *

def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def obtener_puntos(particulas):
    puntos = []
    for particula in particulas:
        x_origen = particula.origen[0]
        y_origen = particula.origen[1]
        x_destino = particula.destino[0]
        y_destino = particula.destino[1]
        punto_origen = (x_origen, y_origen)
        punto_destino = (x_destino, y_destino)
        puntos.append(punto_origen)
        puntos.append(punto_destino)
    return puntos



def puntos_mas_cercanos(particulas)->list:
    resultado = []
    puntos = obtener_puntos(particulas)
    for punto_i in puntos:
        x1 = punto_i[0]
        y1 = punto_i[1]
        min = 1000
        cercano = (0, 0)
        for punto_j in puntos:
            if punto_i != punto_j:
                x2 = punto_j[0]
                y2 = punto_j[1]
                d = distancia_euclidiana(x1, y1, x2, y2)
            #else no hace nada
                if d < min:
                    min = d
                    cercano = (x2, y2)
                #else no hace nada
        
        resultado.append((punto_i, cercano))
    return resultado