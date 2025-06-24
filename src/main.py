from video_pregrabado import extraer_caras
from grabar_modelo import grabar_modelo
from entrenamiento import entrenar_modelo
from prueba import probar_modelo
from admin import mostrar_alumnos, borrar_alumno, editar_informacion

def menu_options():
    print("1. Cargar modelo")
    print("2. Grabar rostros")
    print("3. Entrenar Modelo")
    print("4. Probar Modelo")
    print("5. Salir")
    return input("Seleccione una opción: ")

def menu():
    while True:
        opcion = menu_options()
        if opcion == "1":
            print("formato: video.mp4")
            video_path = input("Ingrese la ruta del video: ")
            codigo = input("Ingrese el código del estudiante: ")
            extraer_caras(video_path, "faces", codigo)
        elif opcion == "2":
            print("Los rostros se guardarán en la carpeta 'faces'")
            print("Mantenga 'p' para empezar a capturar rostros y 'q' para salir de la ventana de video")
            grabar_modelo("faces", input("Ingrese el código del estudiante: "))
        elif opcion == "3":
            entrenar_modelo()
        elif opcion == "4":
            print("Presione 'q' para salir de la ventana de video")
            probar_modelo()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Esta opción no existe, inténtalo de nuevo.")
            
    
def agregar_alumno_menu():
    while True:
        print("\n--- AGREGAR ALUMNO ---")
        print("2.1 Generar qr y capturar rostros con la cámara")
        print("2.2 Generar qr y capturar rostros desde un video pregrabado")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        
        codigo = input("Ingrese el código del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")
        from generar_qr import agregar_alumno

        if opcion == "2.1":
            agregar_alumno(codigo, nombre, carrera)
            print("Mantenga 'p' para empezar a capturar rostros y 'q' para salir de la ventana de video")
            grabar_modelo(f"face_recognition_app/faces/{codigo}", codigo)
            
        elif opcion == "2.2":
            agregar_alumno(codigo, nombre, carrera)
            video_path = input("Ingrese la ruta del video: ")
            extraer_caras(video_path, f"face_recognition_app/faces/{codigo}", codigo)
            
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    
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

if __name__ == '__main__':
    menu()