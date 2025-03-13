import json
import os

ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    """Carga las tareas desde el archivo JSON."""
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r") as f:
            return json.load(f)
    return []

def guardar_tareas(tareas):
    """Guarda las tareas en un archivo JSON."""
    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(tareas, f, indent=4)

def agregar_tarea(tareas):
    """Agrega una nueva tarea."""
    tarea = input("Ingrese la tarea: ")
    tareas.append(tarea)
    guardar_tareas(tareas)
    print("✅ Tarea agregada.")

def ver_tareas(tareas):
    """Muestra todas las tareas."""
    if not tareas:
        print("📭 No hay tareas pendientes.")
    else:
        print("\n📌 Tareas pendientes:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")
    print()

def eliminar_tarea(tareas):
    """Elimina una tarea seleccionada."""
    ver_tareas(tareas)
    try:
        num = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= num < len(tareas):
            tarea_eliminada = tareas.pop(num)
            guardar_tareas(tareas)
            print(f"🗑️ Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada no válida.")

def menu():
    """Menú principal del gestor de tareas."""
    tareas = cargar_tareas()
    while True:
        print("\n📋 GESTOR DE TAREAS")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
