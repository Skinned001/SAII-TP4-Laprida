def mostrar_alumnos(alumnos):
    if not alumnos:
        print("\nNo hay alumnos registrados.")
        return
    
    print("\n" + "="*40)
    print(f"{'ALUMNO':<15} | {'MATERIAS Y NOTAS'}")
    print("-"*40)
    
    for alumno in alumnos:
        nombre = alumno[0]
        materias = alumno[1]
        # Bonus: Calcular promedio para mostrarlo
        notas = [m[1] for m in materias]
        promedio = sum(notas) / len(notas) if notas else 0
        
        info_materias = ", ".join([f"{m[0]}: {m[1]}" for m in materias])
        print(f"{nombre:<15} | {info_materias} (Prom: {promedio:.2f})")
    print("="*40)

def buscar_alumno(nombre, alumnos):
    for i in range(len(alumnos)):
        if alumnos[i][0].lower() == nombre.lower():
            return i
    return None

def gestionar_notas(alumnos, indice=None):
    if indice is None:
        nombre = input("\nIngrese el nombre del alumno para gestionar notas: ")
        indice = buscar_alumno(nombre, alumnos)
        if indice is None:
            print("Alumno no encontrado.")
            return

    materia_nom = input("Ingrese el nombre de la materia: ")
    try:
        nota = int(input("Ingrese la nota: "))
    except ValueError:
        print("Error: La nota debe ser un número entero.")
        return

    materias_actuales = alumnos[indice][1]
    encontrada = False
    for m in materias_actuales:
        if m[0].lower() == materia_nom.lower():
            m[1] = nota
            print(f"Nota de {materia_nom} actualizada para {alumnos[indice][0]}.")
            encontrada = True
            break
    
    if not encontrada:
        materias_actuales.append([materia_nom, nota])
        print(f"Materia {materia_nom} agregada con nota {nota}.")

def agregar_alumno(alumnos):
    nombre = input("\nNombre del nuevo alumno: ")
    indice = buscar_alumno(nombre, alumnos)
    
    if indice is not None:
        print(f"El alumno {nombre} ya existe.")
        op = input("¿Desea modificar sus notas? (s/n): ")
        if op.lower() == 's':
            gestionar_notas(alumnos, indice)
    else:
        alumnos.append([nombre, []])
        print(f"Alumno {nombre} registrado.")
        # Opcional: cargar una primera nota
        gestionar_notas(alumnos, len(alumnos)-1)

def mostrar_mejor_promedio(alumnos):
    if not alumnos: return
    
    # Lista de tuplas (nombre, promedio)
    promedios = []
    for alu in alumnos:
        notas = [m[1] for m in alu[1]]
        prom = sum(notas) / len(notas) if notas else 0
        promedios.append((alu[0], prom))
    
    # Ordenar por promedio (segundo elemento de la tupla) de mayor a menor
    promedios.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\n El mejor alumno es {promedios[0][0]} con un promedio de {promedios[0][1]:.2f}")

def menu():
    # Matriz inicial solicitada
    alumnos = [
        ['Juan', [['Matematicas',8], ['Lengua',9], ['Sociales',7], ['Naturales',7]]],
        ['Ana', [['Lengua',9], ['Matematicas',10], ['Sociales',8], ['Naturales',6]]],
        ['Luis', [['Lengua',6], ['Sociales',8], ['Matematicas',7], ['Naturales',6]]],
        ['María',[['Lengua',9], ['Sociales',10], ['Naturales',10], ['Matematicas',9]]]
    ]

    while True:
        print("\n--- MENÚ DE GESTIÓN ---")
        print("1. Ver alumnos y promedios")
        print("2. Agregar alumno")
        print("3. Agregar o modificar notas")
        print("4. Ver mejor promedio")
        print("5. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            mostrar_alumnos(alumnos)
        elif opcion == "2":
            agregar_alumno(alumnos)
        elif opcion == "3":
            gestionar_notas(alumnos)
        elif opcion == "4":
            mostrar_mejor_promedio(alumnos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()