class Libro_Modelo:
    def __init__(self, fecha, cantidad_hojas, tematica, genero):
        self.fecha = fecha
        self.cantidad_hojas = cantidad_hojas
        self.tematica = tematica
        self.genero = genero

    # GETS
    def get_fecha(self):
        return self.fecha

    def get_cantidad_hojas(self):
        return self.cantidad_hojas

    def get_tematica(self):
        return self.tematica

    def get_genero(self):
        return self.genero

    # SETS
    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_cantidad_hojas(self, cantidad_hojas):
        self.cantidad_hojas = cantidad_hojas

    def set_tematica(self, tematica):
        self.tematica = tematica

    def set_genero(self, genero):
        self.genero = genero

    def mostrar_info(self):
        return (
            f"Libro | Temática: {self.tematica} | "
            f"Género: {self.genero} | Fecha: {self.fecha} | "
            f"Hojas: {self.cantidad_hojas}"
        )
