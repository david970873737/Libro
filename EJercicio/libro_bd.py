class Base_Datos_Libro:
    def __init__(self):
        self.libros = []

    def guardar_libro(self, libro):
        self.libros.append(libro)

    def agregar_varios_libros(self, lista_libros):
        self.libros.extend(lista_libros)

    def insertar_libro(self, libro, index):
        self.libros.insert(index, libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)
        
    def eliminar_por_posicion(self, index):
        return self.libros.pop(index)

    def buscar_posicion(self, libro):
        return self.libros.index(libro)

    def contar_libro(self, libro):
        return self.libros.count(libro)

    def ordenar_por_tematica(self):
        self.libros.sort(key=lambda libro: libro.tematica)

    def invertir_orden(self):
        self.libros.reverse()

    def mostrar_info(self):
        for libro in self.libros:
            print(libro.mostrar_info())
