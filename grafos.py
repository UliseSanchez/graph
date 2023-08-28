from particula import Particula

class Grafo:

    def __init__(self):
        self.__grafo = dict()
    
    def mostrar(self):
        for key, value in self.__grafo.items():
            print(key,value)

    def agregar_nodo(self, p):
        origen = p.origen
        destino = p.destino
        distancia  = p.distancia
        if origen in self.__grafo:
            self.__grafo[origen].append([destino, distancia])
        else:
            self.__grafo[origen] = [[destino, distancia]]

        if destino in self.__grafo:
            self.__grafo[destino].append([origen, distancia])
        else:
            self.__grafo[destino] = [[origen, distancia]]
    
    def __str__(self):
        return "".join(
            str(key)+ " --> "+ str(value) + "\n" for key,value in self.__grafo.items())
