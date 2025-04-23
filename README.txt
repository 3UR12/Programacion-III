---

```markdown
# 📚 Sistema de Gestión de Biblioteca - Programación III

Bienvenido al sistema de gestión de biblioteca desarrollado en Python como parte del curso **Programación III**. Este proyecto aplica los principios de **programación orientada a objetos (POO)** y permite administrar diferentes tipos de materiales bibliográficos de forma sencilla, eficiente y visualmente amigable.

---

## 🚀 Funcionalidades principales

- ✅ Registrar distintos materiales (📘 Libros, 📖 Revistas y 💿 DVDs).
- ✅ Evita duplicados de título y autor dentro de la misma categoría.
- ✅ Mostrar todos los materiales registrados con su tipo y detalles.
- ✅ Buscar materiales fácilmente por título.
- ✅ Guardar el inventario automáticamente.
- ✅ Interfaz por consola con emojis para hacerlo más amigable 🐾.

---

## 🧱 Estructura del proyecto

```bash
biblioteca/
│
├── funciones.py          # Contiene las funciones principales del sistema
├── materiales.py         # Define las clases y herencia POO
├── inventario.json       # Archivo donde se guarda la información (se crea al salir)
├── main.py               # Archivo principal que ejecuta el programa
├── README.md             # Descripción del proyecto (este archivo)
```

---

## 🧠 ¿Cómo funciona?

1. Al iniciar `main.py`, el sistema intenta cargar automáticamente los materiales guardados anteriormente.
2. Muestra un menú principal con las siguientes opciones:
   - **1️⃣ Agregar Material:** Puedes ingresar libros, revistas o DVDs.
   - **2️⃣ Listar Materiales:** Muestra todo el inventario clasificado.
   - **3️⃣ Buscar por Título:** Encuentra materiales rápidamente.
   - **4️⃣ Salir:** Guarda todo de forma segura y cierra el programa.
3. Durante el ingreso de materiales:
   - El sistema evita duplicados si ya existe un material con el mismo **título y autor** dentro de la **misma clasificación**.
4. Los datos se guardan automáticamente en formato JSON.

---

## 🧩 Clases del sistema

Todas las clases están definidas en `materiales.py` siguiendo la estructura POO:

- **MaterialBiblioteca (clase padre):**
  - Atributos comunes: `título`, `autor`, `año_publicación`
  - Método base: `mostrar_informacion()`
- **Libro, Revista, DVD (subclases):**
  - Cada una añade un atributo específico:
    - `Libro`: número de páginas
    - `Revista`: número de edición
    - `DVD`: duración en minutos
  - Todas sobrescriben `mostrar_informacion()` para incluir su atributo adicional y tipo.

---

## 💾 Guardado de datos

Los materiales son guardados automáticamente al salir del programa en el archivo `inventario.json`. Si ocurre un error durante el guardado, se informa al usuario con un mensaje detallado sin interrumpir la ejecución.

---

## 🐛 Manejo de errores

- Entrada inválida en el menú ➡️ Mensaje de advertencia.
- Problemas al guardar el archivo ➡️ Notificación con detalles del error.

---

## 🖥️ Cómo ejecutar el programa

1. Asegúrate de tener Python instalado.
2. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/biblioteca.git
   cd biblioteca
   ```
3. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

---

## ✨ Créditos

Desarrollado por 3UR12 como parte del curso **Programación III**. Este proyecto busca demostrar el uso práctico de POO y estructuras de control en Python de forma clara, funcional y agradable para el usuario final.

---

## 🐾 ¡Gracias por visitar la biblioteca virtual!

```

---

