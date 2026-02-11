from libro_modelo import Libro_Modelo
from libro_bd import Base_Datos_Libro
from Autores import Autor
from api_datos_autores import Api_Lista_Autores

# ===== AUTORES =====
api_autores = Api_Lista_Autores()

autor1 = Autor("Masculino", "David Reyes", "18", "31/01/2008", "Colombiano")

autor2 = Autor( "Masculino", "Juan Suarez", "24", "01/09/2002", "Colombiano")

api_autores.guardar_autor(autor1)
api_autores.guardar_autor(autor2)

print("\n=== AUTORES ===")
api_autores.mostrar_autores()



print("\n===EXTENDER LISTA DE AUTORES===")

autor3 = Autor("Femenino", "Patricia Cuellar", "28", "12/05/1997", "Colombiana")
autor4 = Autor("masculino", "Pepe Perez", "35", "20/10/1988", "Colombiano")

extender_lista = [autor3, autor4]
api_autores.agregar_varios_autores(extender_lista)
api_autores.mostrar_autores()



print("\n===INSERTAR AUTOR EN POSICIÓN 1===")
autor5 = Autor("Femenino", "Sandra", "22", "05/03/2001", "Colombiana")
api_autores.insertar_autor(1, autor5)
api_autores.mostrar_autores()



print("\n===BUSCAR POSICIÓN DE UN AUTOR===")

posicion = api_autores.buscar_posicion(autor1)
print(f"Posición de {autor1.get_nombre()}: {posicion}")



print("\n=== CONTAR AUTOR ===")

cantidad = api_autores.contar_autor(autor1)
print(f"veces que aparece {autor1.get_nombre()}: {cantidad}")



print("\n=== REMOVER AUTOR EN POSICIÓN 2 ===")
api_autores.eliminar_autor(autor2)
api_autores.mostrar_autores()



print("\n===POP===")
autor_removido = api_autores.eliminar_por_posicion(0)
print("Autor removido:", autor_removido.get_nombre())
api_autores.mostrar_autores()



print("\n=== AUTORES ORDENADOS POR NOMBRE ===")
api_autores.ordenar_autores()
api_autores.mostrar_autores()



print("\n=== AUTORES EN ORDEN INVERTIDO ===")
api_autores.invertir_autores()
api_autores.mostrar_autores()
  


# ===== LIBROS =====
bd_libros = Base_Datos_Libro()

libro1 = Libro_Modelo("27/11/2017", 250, "Ciencia ficción", "Ficción")
libro2 = Libro_Modelo("08/03/2005", 60, "Ciencia", "Educativo")
libro3 = Libro_Modelo("14/07/2023", 50, "Anime", "Fantasía")
libro4 = Libro_Modelo("16/11/1999", 90, "Romance", "Romantico")

bd_libros.guardar_libro(libro1)
bd_libros.guardar_libro(libro2)
bd_libros.guardar_libro(libro3)
bd_libros.guardar_libro(libro4)

print("\n=== LIBROS ===")
bd_libros.mostrar_info()

print("\n=== EXTENDER LISTA DE LIBROS ===")
libro5 = Libro_Modelo("01/01/2010", 120, "Historia", "Educativo")
libro6 = Libro_Modelo("20/05/2015", 80, "Aventura", "Ficción")
extender_libros = [libro5, libro6]
bd_libros.agregar_varios_libros(extender_libros)
bd_libros.mostrar_info()



print("\n=== INSERTAR LIBRO EN POSICIÓN 2 ===")
libro7 = Libro_Modelo("10/10/2020", 200, "Misterio", "Suspenso")
bd_libros.insertar_libro(libro7, 2)
bd_libros.mostrar_info()



print ("\n=== REMOVER LIBRO POR POSICION 2 ===")
bd_libros.eliminar_libro(libro2)
bd_libros.mostrar_info()



print("\n=== POP ===")
libro_removido = bd_libros.eliminar_por_posicion(1)
print("Libro removido:", libro_removido.get_tematica())
bd_libros.mostrar_info()



print ("\n=== BUSCAR POSICIÓN DE UN LIBRO ===")
posicion = bd_libros.buscar_posicion(libro1)
print(f"Posición de {libro1.get_tematica()}: {posicion}")



print("\n=== CONTAR LIBRO ===")
cantidad = bd_libros.contar_libro(libro1)
print(f"veces que aparece {libro1.get_tematica()}: {cantidad}")



print("\n=== LIBROS ORDENADOS POR TEMÁTICA ===")
bd_libros.ordenar_por_tematica()
bd_libros.mostrar_info()

print("\n=== LIBROS EN ORDEN INVERTIDO ===")
bd_libros.invertir_orden()
bd_libros.mostrar_info()

