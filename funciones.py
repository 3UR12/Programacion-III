from Materiales import Libro, Revista, DVD
import json

# Lista para guardar los materiales
inventario = []

# Función para agregar material al inventario
def agregar_material():
    while True:
        print("\nSeleccione el tipo de material:")
        print("1. Libro")
        print("2. Revista")
        print("3. DVD")
        print("0. Cancelar")
        opcion = input("Opción: ").strip()

        if opcion == "0":
            print("Operación cancelada.")
            return

        if opcion not in ["1", "2", "3"]:
            print("⚠️ Opción inválida. Intente de nuevo.")
            continue

        titulo = input("Título: ").strip()  # Título del material
        autor = input("Autor: ").strip()    # Autor del material

        # Verificación: ¿ya existe un material con ese título y autor?
                # Verificación: ¿ya existe un material del mismo tipo con ese título y autor?
        for material in inventario:     
            if (
                material.titulo.lower() == titulo.lower() and   
                material.autor.lower() == autor.lower() and
                (
                    (opcion == "1" and isinstance(material, Libro)) or
                    (opcion == "2" and isinstance(material, Revista)) or
                    (opcion == "3" and isinstance(material, DVD))
                )
            ):
                print("❌ Ya existe un material del mismo tipo con ese título y autor.")
                return


        try:
            año = int(input("Año de publicación: "))
        except ValueError:
            print("⚠️ El año debe ser un número entero.")
            return

        try:
            if opcion == "1":
                paginas = int(input("Número de páginas: "))
                inventario.append(Libro(titulo, autor, año, paginas))
                print("✅ Libro agregado exitosamente.")
            elif opcion == "2":
                edicion = int(input("Número de edición: "))
                inventario.append(Revista(titulo, autor, año, edicion))
                print("✅ Revista agregada exitosamente.")
            elif opcion == "3":
                duracion = int(input("Duración en minutos: "))
                inventario.append(DVD(titulo, autor, año, duracion))
                print("✅ DVD agregado exitosamente.")
        except ValueError:
            print("⚠️ Debe ingresar un número entero válido para ese campo.")
        
        break

# Función para listar todos los materiales
def listar_materiales():
    if not inventario:  # Verifica si la lista de inventario está vacía
        print("\n📭 No hay materiales registrados.")
    else:
        print("\n📚 Inventario de materiales:")
        for material in inventario:
            print("-" * 40)
            material.mostrar_informacion()

# Función para buscar un material por su título
def buscar_material():
    if not inventario:
        print("📭 No hay materiales en el inventario.")
        return

    titulo_buscado = input("Ingrese el título del material a buscar: ").strip()
    encontrado = False

    for material in inventario:
        if material.titulo.lower() == titulo_buscado.lower():
            if not encontrado:
                print("\n🔍 Material(es) encontrado(s):")
                print("-" * 40)
            material.mostrar_informacion()  # Mostrar información
            print("-" * 40)
            encontrado = True

    if not encontrado:
        print("❌ Material no encontrado.")


def guardar_inventario(nombre_archivo="inventario.json"):
    datos = []
    for material in inventario:
        item = {
            "tipo": material.tipo,
            "titulo": material.titulo,
            "autor": material.autor,
            "año_publicacion": material.año_publicacion
        }
        if isinstance(material, Libro):
            item["numero_paginas"] = material.numero_paginas
        elif isinstance(material, Revista):
            item["numero_edicion"] = material.numero_edicion
        elif isinstance(material, DVD):
            item["duracion"] = material.duracion
        datos.append(item)
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print("💾 Inventario guardado correctamente.")


def cargar_inventario(nombre_archivo="inventario.json"):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                tipo = item["tipo"]
                titulo = item["titulo"]
                autor = item["autor"]
                año = item["año_publicacion"]
                if tipo == "Libro":
                    inventario.append(Libro(titulo, autor, año, item["numero_paginas"]))
                elif tipo == "Revista":
                    inventario.append(Revista(titulo, autor, año, item["numero_edicion"]))
                elif tipo == "DVD":
                    inventario.append(DVD(titulo, autor, año, item["duracion"]))
    except FileNotFoundError:
        print("📂 No se encontró inventario previo. Se iniciará uno nuevo.")
