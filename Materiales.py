# Clase base para todos los materiales de la biblioteca
class MaterialBiblioteca:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")

# Subclase que representa un Libro
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_paginas = numero_paginas
        self.tipo = "Libro"

    def mostrar_informacion(self):
        print(f"📘 Tipo: {self.tipo}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")
        print(f"Número de páginas: {self.numero_paginas}")

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_edicion):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_edicion = numero_edicion
        self.tipo = "Revista"

    def mostrar_informacion(self):
        print(f"🗞️ Tipo: {self.tipo}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")
        print(f"Número de edición: {self.numero_edicion}")

class DVD(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, duracion):
        super().__init__(titulo, autor, año_publicacion)
        self.duracion = duracion
        self.tipo = "DVD"

    def mostrar_informacion(self):
        print(f"💿 Tipo: {self.tipo}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")
        print(f"Duración (minutos): {self.duracion}")
