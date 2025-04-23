# Clase base para todos los materiales de la biblioteca
class MaterialBiblioteca:   
    def __init__(self, titulo, autor, año_publicacion): # Constructor de la clase MaterialBiblioteca o tambien llamados atributos de la clase
        self.titulo = titulo # Título del material y atributo de la clase
        self.autor = autor  # Autor del material y atributo de la clase
        self.año_publicacion = año_publicacion # Año de publicación del material

    def mostrar_informacion(self):  # Método para mostrar información del material
        print(f"Título: {self.titulo}") #aqui se muestra el titulo del material
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")

class Libro(MaterialBiblioteca):    # Subclase que representa un Libro
    def __init__(self, titulo, autor, año_publicacion, numero_paginas): # Constructor de la clase Libro
        super().__init__(titulo, autor, año_publicacion)    # Llama al constructor de la clase padre
        self.numero_paginas = numero_paginas        # Número de páginas del libro y atributo de la clase
        self.tipo = "Libro"     
        # Inicializa el tipo de material como "Libro"
    
    def mostrar_informacion(self):# Sobrescribe el método para mostrar información específica del libro
        print(f"📘 Tipo: {self.tipo}") #aqui se muestra el tipo de material
        print(f"Título: {self.titulo}") #aqui se muestra el titulo del libro
        print(f"Autor: {self.autor}")   #aqui se muestra el autor del libro
        print(f"Año de publicación: {self.año_publicacion}")    #aqui se muestra el año de publicacion del libro
        print(f"Número de páginas: {self.numero_paginas}")  #aqui se muestra el numero de paginas del libro

class Revista(MaterialBiblioteca):  # Subclase que representa una Revista
    def __init__(self, titulo, autor, año_publicacion, numero_edicion): # Constructor de la clase Revista
        super().__init__(titulo, autor, año_publicacion)    # Llama al constructor de la clase padre
        self.numero_edicion = numero_edicion    # Número de edición de la revista y atributo de la clase
        self.tipo = "Revista"   # Inicializa el tipo de material como "Revista"

    def mostrar_informacion(self):  # Sobrescribe el método para mostrar información específica de la revista
        #aqui se muestra el tipo de material
        print(f"🗞️ Tipo: {self.tipo}")     
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")
        print(f"Número de edición: {self.numero_edicion}")

class DVD(MaterialBiblioteca):  # Subclase que representa un DVD
    def __init__(self, titulo, autor, año_publicacion, duracion):
        super().__init__(titulo, autor, año_publicacion)
        self.duracion = duracion
        self.tipo = "DVD"

    def mostrar_informacion(self):  # Sobrescribe el método para mostrar información específica del DVD
        print(f"💿 Tipo: {self.tipo}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")
        print(f"Duración (minutos): {self.duracion}")
