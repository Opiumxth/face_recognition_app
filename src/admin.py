import csv
import os

ALUMNOS_FILE = os.path.join(os.path.dirname(__file__), "..", "alumnos.csv")

def mostrar_alumnos():
    with open(ALUMNOS_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print("Alumnos registrados:")
        for row in reader:
            print(f"Código: {row['codigo']} | Nombre: {row['nombre']} | Carrera: {row['carrera']}")

def borrar_alumno(codigo):
    rows = []
    with open(ALUMNOS_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader if row['codigo'] != codigo]

    with open(ALUMNOS_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['codigo', 'nombre', 'carrera']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Alumno con código {codigo} eliminado.")

def editar_informacion(codigo, nuevo_nombre=None, nueva_carrera=None):
    actualizado = False
    rows = []
    with open(ALUMNOS_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['codigo'] == codigo:
                if nuevo_nombre: row['nombre'] = nuevo_nombre
                if nueva_carrera: row['carrera'] = nueva_carrera
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