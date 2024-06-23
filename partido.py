class Partido:
    def __init__(self, equipo_local, equipo_visitante, estadio, fecha, hora):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.estadio = estadio
        self.fecha = fecha
        self.hora = hora

    def mostrar_info(self):
        return (f"{self.fecha} {self.hora}: {self.equipo_local.nombre} vs {self.equipo_visitante.nombre} en "
                f"{self.estadio}")
