import json
from particula import Particula
from algoritmos import obtener_puntos
from grafos import Grafo

class Administrador_Particulas:
    def __init__(self):
        self.__particulas = []
        self.__grafo = Grafo()
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
        self.__grafo.agregar_nodo(particula)

    
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0,particula)
        self.__grafo.agregar_nodo(particula)
    
    def mostrar(self):
        for p in self.__particulas:
            print(p)
    
    def mostrar_grafo(self):
        return str(self.__grafo)

    def __str__(self):
        return "".join(
            str(p) + "\n" for p in self.__particulas        
        )
    
    def __len__(self):
        return(
            len(self.__particulas)
        )

    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        
        else:
            raise StopIteration

    def guardar_Archivo(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dictionary() for particula in self.__particulas]
                json.dump(lista, archivo, indent = 5)
                return 1
        except:
            return 0

    def abrir_Archivo(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                self.crear_grafo()
                return 1
        except:
            return 0
            
    def crear_grafo(self):
        for p in self.__particulas:
            self.__grafo.agregar_nodo(p)

    def __lt__(self,other):
        return self.__particulas.velocidad < other.velocidad

    
    def ordenar_por_id(self):
        self.__particulas.sort(key=lambda particula:particula.id)

    def ordenar_por_distancia(self):
        self.__particulas.sort(key=lambda particula:particula.distancia, reverse=True)
    
    def ordenar_por_velocidad(self):
        self.__particulas.sort(key = lambda particula:particula.velocidad)





            


