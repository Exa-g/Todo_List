import json

def cargar_tareas():
    try:
        with open("tasks.txt", "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
    
def guardar_tareas(lista_tareas):
    with open("tasks.txt", "w") as archivo:
        json.dump(lista_tareas, archivo)
        
def agregar_tarea(tarea, lista_tareas):
    lista_tareas.append({"tarea": tarea, "completada": False})
    
def marcar_completada(numero_tarea, lista_tareas):
    try:
        numero_tarea = int(numero_tarea)
        if 1 <= numero_tarea <= len(lista_tareas):
            lista_tareas[numero_tarea - 1]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Numero de tarea no valido.")
            
    except ValueError:
        print("Por favor, ingrese un numero valido.")
        
def mostrar_tareas(lista_tareas):
    print("\n=== Lista de Tareas ===")
    for i, tarea in enumerate(lista_tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['tarea']} ({estado})")
        
def main():
    lista_tareas = cargar_tareas()
    
    while True:
        mostrar_tareas(lista_tareas)
        
        opcion = input("\n1. Agregar tarea\n2. Marcar Tarea como Completada\n3. Salir\n\nElije una opcion: ")
        
        if opcion == "1":
            nueva_tarea = input("Ingrese la nueva tarea: ")
            agregar_tarea(nueva_tarea, lista_tareas)
            guardar_tareas(lista_tareas)
            
        elif opcion == "2":
            numero_tarea = input("Ingresa el numero de tarea a marcar como completada: ")
            marcar_completada(numero_tarea, lista_tareas)
            guardar_tareas(lista_tareas)
            
        elif opcion == "3":
            break
        
        else: print("Opcion no valida. Intentelo de nuevo.")
        
if __name__ == "__main__":
    main()