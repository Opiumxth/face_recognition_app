from admin import mostrar_alumnos, borrar_alumno, editar_informacion

def panel_administracion():
    while True:
        print("\n--- PANEL DE ADMINISTRACIÓN ---")
        print("3.1 Ver información de alumnos")
        print("3.2 Borrar alumno")
        print("3.3 Editar información")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "3.1":
            mostrar_alumnos()
        elif opcion == "3.2":
            codigo = input("Ingrese el código del alumno a eliminar: ")
            borrar_alumno(codigo)
        elif opcion == "3.3":
            codigo = input("Ingrese el código del alumno a editar: ")
            nuevo_nombre = input("Nuevo nombre (dejar vacío si no desea cambiar): ")
            nueva_carrera = input("Nueva carrera (dejar vacío si no desea cambiar): ")
            editar_informacion(codigo, nuevo_nombre or None, nueva_carrera or None)
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
# panel_administracion()
# para probarlo uwu