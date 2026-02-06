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

print("=== AUTORES ===")
api_autores.mostrar_autores()

print("=== AUTORES ORDENADOS POR NOMBRE ===")
api_autores.ordenar_autores()
api_autores.mostrar_autores()

print("=== AUTORES EN ORDEN INVERTIDO ===")
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

print("\n=== LIBROS ORDENADOS POR TEMÁTICA ===")
bd_libros.ordenar_por_tematica()
bd_libros.mostrar_info()

print("\n=== LIBROS EN ORDEN INVERTIDO ===")
bd_libros.invertir_orden()
bd_libros.mostrar_info()

