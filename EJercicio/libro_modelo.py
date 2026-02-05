class Libro_Modelo:
    def __init__(self, fecha, cantidad_hojas, tematica, genero):
        self.fecha = fecha
        self.cantidad_hojas = cantidad_hojas
        self.tematica = tematica
        self.genero = genero

    def get_fecha(self):
        return self.fecha

    def get_tematica(self):
        return self.tematica

    def mostrar_info(self):
        return f"Libro | Temática: {self.tematica} | Fecha: {self.fecha} | Hojas: {self.cantidad_hojas}"
