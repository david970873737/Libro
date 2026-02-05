class Api_Lista_Autores:
    def __init__(self):
        self.lista_autores = []

    def guardar_autor(self, autor):
        self.lista_autores.append(autor)

    def mostrar_autores(self):
        for autor in self.lista_autores:
            print(autor.ver_info())
