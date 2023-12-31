from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id = "0", origen_x = 0, origen_y = 0, destino_x = 0, destino_y = 0, velocidad = 0, red = 0, green = 0, blue = 0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x, destino_x,origen_y, destino_y)

    def __str__(self):
        return(
            "ID:        " + str(self.__id) +"\n"+
            "Origen:    (" + str(self.__origen_x)+","+str(self.__origen_y) + ")\n"+
            "Destino:   (" + str(self.__destino_x)+","+str(self.__destino_y) + ")\n"+
            "Velocidad: " + str(self.__velocidad) + "\n"+
            "Distancia: " + str(self.__distancia) + "\n"+
            "Color      (" + str(self.__red)+","+str(self.__green)+","+str(self.__blue) + ")\n"
        )

    @property
    def id(self):
        return self.__id
    
    @property
    def origen(self):
        return (self.__origen_x, self.__origen_y)
    
    @property
    def destino(self):
        return (self.__destino_x, self.__destino_y)
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def distancia(self):
        return self.__distancia
    
    @property
    def color(self):
        return (self.__red, self.__green, self.__blue)
    
    def to_dictionary(self):
        return{
            'id': self.__id,
            'origen_x': self.__origen_x,
            'origen_y': self.__origen_y,
            'destino_x': self.__destino_x,
            'destino_y': self.__destino_y,
            'red': self.__red,
            'green': self.__green,
            'blue': self.__blue,
            'velocidad': self.__velocidad
        }
