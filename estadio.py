class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

    def __str__(self):
        return f"{self.nombre}, {self.ciudad} (Capacidad: {self.capacidad})"
