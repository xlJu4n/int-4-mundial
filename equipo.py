class Equipo:
    def __init__(self, nombre, ganados, empatados, perdidos):
        self.nombre = nombre
        self.ganados = ganados
        self.empatados = empatados
        self.perdidos = perdidos

    def __str__(self):
        return f"{self.nombre} (G: {self.ganados}, E: {self.empatados}, P: {self.perdidos})"
