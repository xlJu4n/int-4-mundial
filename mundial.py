import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from equipo import Equipo
from grupo import Grupo
from estadio import Estadio
from partido import Partido

class Mundial(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mundial 2034")
        self.geometry("1200x800")

        self.grupos = {}
        self.partidos = []
        self.equipos = []

     
        panel = ttk.Frame(self)
        panel.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    
        frame_botones = ttk.Frame(panel)
        frame_botones.pack(side=tk.LEFT, fill=tk.Y)

       
        datos_btn = ttk.Button(frame_botones, text="Datos", command=self.load_data)
        datos_btn.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        partidos_btn = ttk.Button(frame_botones, text="Partidos", command=self.mostrar_partidos)
        partidos_btn.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        
        self.combo = ttk.Combobox(panel)
        self.combo.pack(side=tk.TOP, fill=tk.X, padx=15, pady=15)
        self.combo.bind("<<ComboboxSelected>>", self.mostrar_info_equipo)

       
        self.info_text = ScrolledText(panel, wrap=tk.WORD, state=tk.DISABLED)
        self.info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def load_data(self):
        grupo_a = Grupo("Grupo A")
        grupo_a.agregar_equipo(Equipo("Argentina", 3, 1, 1))
        grupo_a.agregar_equipo(Equipo("Corea del Sur", 1, 3, 1))
        grupo_a.agregar_equipo(Equipo("Nigeria", 1, 2, 1))
        grupo_a.agregar_equipo(Equipo("Bosnia Herzegovina", 1, 1, 2))

        grupo_b = Grupo("Grupo B")
        grupo_b.agregar_equipo(Equipo("Alemania", 3, 1, 1))
        grupo_b.agregar_equipo(Equipo("Portugal", 1, 3, 1))
        grupo_b.agregar_equipo(Equipo("China", 1, 1, 1))
        grupo_b.agregar_equipo(Equipo("Camerun", 1, 0, 0))

        grupo_c = Grupo("Grupo C")
        grupo_c.agregar_equipo(Equipo("Ecuador", 3, 1, 0))
        grupo_c.agregar_equipo(Equipo("Italia", 3, 3, 1))
        grupo_c.agregar_equipo(Equipo("Australia", 1, 0, 1))
        grupo_c.agregar_equipo(Equipo("Iran", 0, 1, 1))

        grupo_d = Grupo("Grupo D")
        grupo_d.agregar_equipo(Equipo("España", 3, 3, 1))
        grupo_d.agregar_equipo(Equipo("Uruguay", 3, 1, 0))
        grupo_d.agregar_equipo(Equipo("Estados Unidos", 1, 1, 1))
        grupo_d.agregar_equipo(Equipo("Croacia", 1, 3, 0))

        self.grupos = {
            "Grupo A": grupo_a,
            "Grupo B": grupo_b,
            "Grupo C": grupo_c,
            "Grupo D": grupo_d
        }

        estadio1 = Estadio("El Monumental", "Ciudad de Buenos Aires", 50000)
        estadio2 = Estadio("La Bombonera", "Buenos Aires", 70000)
        estadio3 = Estadio("Mario Alberto Kempes", "Cordoba", 57000)
        estadio4 = Estadio("Libertadores de America", "Buenos Aires", 48069)
        estadio5 = Estadio("Ciudad de la Plata", "Buenos Aires", 53000)
        estadio6 = Estadio("Marcelo Bielsa", "Santa Fe", 43000)

        self.partidos = [
            Partido(grupo_a.get_equipos()[0], grupo_a.get_equipos()[1], estadio1, "2034-06-10", "10:00"),
            Partido(grupo_a.get_equipos()[0], grupo_a.get_equipos()[2], estadio2, "2034-06-13", "14:00"),
            Partido(grupo_a.get_equipos()[0], grupo_a.get_equipos()[3], estadio3, "2034-06-16", "18:00"),
            Partido(grupo_a.get_equipos()[1], grupo_a.get_equipos()[2], estadio4, "2034-06-11", "10:00"),
            Partido(grupo_a.get_equipos()[1], grupo_a.get_equipos()[3], estadio5, "2034-06-14", "12:00"),
            Partido(grupo_a.get_equipos()[2], grupo_a.get_equipos()[3], estadio6, "2034-06-17", "14:00"),
            Partido(grupo_b.get_equipos()[0], grupo_b.get_equipos()[1], estadio6, "2034-06-11", "16:00"),
            Partido(grupo_b.get_equipos()[0], grupo_b.get_equipos()[2], estadio4, "2034-06-14", "15:00"),
            Partido(grupo_b.get_equipos()[0], grupo_b.get_equipos()[3], estadio1, "2034-06-17", "17:00"),
            Partido(grupo_b.get_equipos()[1], grupo_b.get_equipos()[2], estadio5, "2034-06-17", "10:00"),
            Partido(grupo_b.get_equipos()[1], grupo_b.get_equipos()[3], estadio3, "2034-06-20", "14:00"),
            Partido(grupo_b.get_equipos()[2], grupo_b.get_equipos()[3], estadio2, "2034-06-23", "12:00"),
            Partido(grupo_c.get_equipos()[0], grupo_c.get_equipos()[1], estadio6, "2034-06-21", "16:00"),
            Partido(grupo_c.get_equipos()[0], grupo_c.get_equipos()[2], estadio2, "2034-06-24", "12:00"),
            Partido(grupo_c.get_equipos()[0], grupo_c.get_equipos()[3], estadio5, "2034-06-30", "14:00"),
            Partido(grupo_c.get_equipos()[1], grupo_c.get_equipos()[2], estadio1, "2034-06-26", "10:00"),
            Partido(grupo_c.get_equipos()[1], grupo_c.get_equipos()[3], estadio3, "2034-06-20", "10:00"),
            Partido(grupo_c.get_equipos()[2], grupo_c.get_equipos()[3], estadio4, "2034-06-29", "18:00"),
            Partido(grupo_d.get_equipos()[0], grupo_d.get_equipos()[1], estadio2, "2034-06-16", "15:00"),
            Partido(grupo_d.get_equipos()[0], grupo_d.get_equipos()[2], estadio5, "2034-06-17", "19:00"),
            Partido(grupo_d.get_equipos()[0], grupo_d.get_equipos()[3], estadio4, "2034-06-19", "18:00"),
            Partido(grupo_d.get_equipos()[1], grupo_d.get_equipos()[2], estadio6, "2034-06-23", "10:00"),
            Partido(grupo_d.get_equipos()[1], grupo_d.get_equipos()[3], estadio5, "2034-06-20", "15:00"),
            Partido(grupo_d.get_equipos()[0], grupo_d.get_equipos()[1], estadio1, "2034-06-22", "18:00"),
            Partido(grupo_d.get_equipos()[0], grupo_d.get_equipos()[2], estadio6, "2034-06-25", "09:00"),
            Partido(grupo_d.get_equipos()[0], grupo_d.get_equipos()[3], estadio3, "2034-06-28", "15:00"),
            Partido(grupo_d.get_equipos()[1], grupo_d.get_equipos()[2], estadio4, "2034-06-28", "19:00"),
            Partido(grupo_d.get_equipos()[1], grupo_d.get_equipos()[3], estadio1, "2034-07-01", "10:00"),
            Partido(grupo_d.get_equipos()[2], grupo_d.get_equipos()[3], estadio4, "2034-06-03", "15:00")
        ]

        self.equipos = []
        for grupo in self.grupos.values():
            self.equipos.extend(grupo.get_equipos())

        self.combo['values'] = [equipo.nombre for equipo in self.equipos]
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, "Datos cargados.\n\n")
        self.info_text.config(state=tk.DISABLED)
        

    def mostrar_info_equipo(self, event=None):
        equipo_nombre = self.combo.get()
        equipo = next((e for e in self.equipos if e.nombre == equipo_nombre), None)
        if equipo:
            self.info_text.config(state=tk.NORMAL)
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, f"Nombre del Equipo: {equipo.nombre}\n\n")
            self.info_text.insert(tk.END, "Partidos:\n\n")
            for partido in self.partidos:
                if partido.equipo_local == equipo or partido.equipo_visitante == equipo:
                    self.info_text.insert(tk.END, f"{partido.mostrar_info()}\n\n")
            self.info_text.config(state=tk.DISABLED)

    def mostrar_partidos(self):
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        for partido in self.partidos:
            self.info_text.insert(tk.END, f"{partido.mostrar_info()}\n")
            self.info_text.insert(tk.END, "-"*30 + "\n")
        self.info_text.config(state=tk.DISABLED)
