import time
from funciones import agregar_material, listar_materiales, buscar_material, cargar_inventario, guardar_inventario
cargar_inventario()

# Función principal del menú
def menu():
    while True:
        print("\n" + "🐾" * 18 )
        print("      🏛️ MENÚ DE BIBLIOTECA 🏛️")
        print("🐾" * 18)
        print("1️⃣  ➕ Agregar Material")
        print("2️⃣  📋 Lista de Materiales")
        print("3️⃣  🔍 Buscar por Título")
        print("4️⃣  🚪 Salir")
        print("-" * 18)
        opcion = input("Seleccione una opción (1-4): ")

        # Opciones del menú
        if opcion == "1":
            agregar_material()
        elif opcion == "2":
            listar_materiales()
        elif opcion == "3":
            buscar_material()
        elif opcion == "4":
            print("🔄 Guardando materiales...")
            time.sleep(1)
            try:
                guardar_inventario()
            except Exception as e:
                print("⚠️ Ocurrió un error al guardar los materiales.")
                print(f"🛠️ Detalles del error: {e}")
                
            print("\n👋 ¡Gracias por usar la biblioteca!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")
    
# Ejecutar el menú principal
menu()