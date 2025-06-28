import csv
import os
import shutil

ALUMNOS_FILE = os.path.join(os.path.dirname(__file__), "..", "face_recognition_app/alumnos.csv")

CARRERAS = {
    '0': 'Mantener carrera actual',
    '1': 'Ingeniería de Sistemas',
    '2': 'Ingeniería de Software',
    '3': 'Ciencias de la Computación'
}

def elegir_carrera():
    print("Elige una carrera:")
    for clave, nombre in CARRERAS.items():
        print(f"{clave}. {nombre}")
    opcion = input("Opción: ")
    return CARRERAS.get(opcion, None)


def mostrar_alumnos():
    with open(ALUMNOS_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print("Alumnos registrados:")
        for row in reader:
            print(f"Código: {row['codigo']} | Nombre: {row['nombre']} | Carrera: {row['carrera']}")

def borrar_alumno(codigo):
    encontrado = False
    rows = []
    with open(ALUMNOS_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['codigo'] == codigo:
                encontrado = True
            else:
                rows.append(row)

    if not encontrado:
        print("Alumno no encontrado.")
        return

    with open(ALUMNOS_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['codigo', 'nombre', 'carrera']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        CARPETAS_ALUMNOS = os.path.join(os.path.dirname(__file__), "..", "face_recognition_app/faces")
        carpeta_alumno = os.path.join(CARPETAS_ALUMNOS, codigo)
        if os.path.exists(carpeta_alumno):
            shutil.rmtree(carpeta_alumno)
            print(f"Carpeta del alumno {codigo} eliminada.")
        else:
            print(f"No se encontró carpeta para el alumno {codigo}.")
    print(f"Alumno con código {codigo} eliminado.")

def editar_informacion(codigo, nuevo_nombre=None, nueva_carrera=None):
    actualizado = False
    rows = []
    with open(ALUMNOS_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['codigo'] == codigo:
                if nuevo_nombre:
                    row['nombre'] = nuevo_nombre
                if nueva_carrera:
                    row['carrera'] = elegir_carrera()
                actualizado = True
            rows.append(row)

    if actualizado:
        with open(ALUMNOS_FILE, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['codigo', 'nombre', 'carrera']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Alumno con código {codigo} actualizado.")
    else:
        print("Código no encontrado.")