class Autor:
    def __init__(self, genero, nombre, edad, fecha_nacimiento, nacionalidad):
        self.genero = genero
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad

    # GETS
    def get_genero(self):
        return self.genero

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_nacionalidad(self):
        return self.nacionalidad

    # SETS
    def set_genero(self, genero):
        self.genero = genero

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        return (
            f"{self.nombre} | {self.genero} | {self.edad} años | "
            f"Nacido: {self.fecha_nacimiento} | {self.nacionalidad}"
        )
