class Api_Lista_Autores:
    def __init__(self):
        self.autores = []

    def guardar_autor(self, autor):
        self.autores.append(autor)

    def agregar_varios_autores(self, lista_autores):
        self.autores.extend(lista_autores)

    def insertar_autor(self,posicion, autor):
        self.autores.insert(posicion, autor)

    def eliminar_autor(self, autor):
        self.autores.remove(autor)

    def eliminar_por_posicion(self, posicion):
        return self.autores.pop(posicion)

    def buscar_posicion(self, autor):
        return self.autores.index(autor)

    def contar_autor(self, autor):
        return self.autores.count(autor)

    def ordenar_autores(self):
        self.autores.sort(key=lambda autor: autor.get_nombre())

    def invertir_autores(self):
        self.autores.reverse()

    def mostrar_autores(self):
        for autor in self.autores:
            print(autor.mostrar_info())
