from libro_modelo import Libro_Modelo
from libro_bd import Base_Datos_Libro
from Autores import Autor
from api_datos_autores import Api_Lista_Autores

# Autores
api_autores = Api_Lista_Autores()
autor1 = Autor("Masculino", "David Reyes", 18, "31/01/2008", "Colombiano")
autor2 = Autor("Masculino", "Juan Suarez", 24, "01/09/2002", "Colombiano")

api_autores.guardar_autor(autor1)
api_autores.guardar_autor(autor2)

print("=== AUTORES ===")
api_autores.mostrar_autores()

# Libros
bd = Base_Datos_Libro()

libro1 = Libro_Modelo("27/11/2017", 250, "Ciencia ficción", "Ficción")
libro2 = Libro_Modelo("08/03/2005", 60, "Ciencia", "Educativo")
libro3 = Libro_Modelo("14/07/2023", 50, "Anime", "Fantasía")

bd.guardar_libro(libro1)
bd.guardar_libro(libro2)
bd.guardar_libro(libro3)

print("=== LIBROS ===")
bd.mostrar_info()

print("=== ORDENADOS POR TEMÁTICA ===")
bd.ordenar_por_tematica()
bd.mostrar_info()

print("=== ORDEN INVERTIDO ===")
bd.invertir_orden()
bd.mostrar_info()

