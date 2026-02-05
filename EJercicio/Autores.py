class Autor:
    def __init__(self, genero, nombre, edad, fecha_nacimiento, nacionalidad=""):
        self.genero = genero
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
    

    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

  
    def ver_info(self):
        return f"Autor: {self.nombre} | Nac: {self.fecha_nacimiento} |"
