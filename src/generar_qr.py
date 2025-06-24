import qrcode
import os
import csv

def generar_qr(qr_file, codigo):
    # Crear el directorio si no existe
    os.makedirs(qr_file, exist_ok=True)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(codigo)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{qr_file}/qr_{codigo}.png")
    print(f"QR code generado y guardado como qr_{codigo}.png en {qr_file}")

def guardar_datos(csv_file, codigo, nombre, carrera):

    file_exists = os.path.isfile(csv_file)
    file_is_empty = not file_exists or os.path.getsize(csv_file) == 0

    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        campos = ["codigo", "nombre", "carrera"]
        escritor = csv.DictWriter(file, fieldnames=campos)

        if file_is_empty:
            escritor.writeheader()

        escritor.writerow({
            "codigo": codigo,
            "nombre": nombre,
            "carrera": carrera,
        })
        print("Datos del estudiante guardados.")

def agregar_alumno(codigo,nombre,carrera):
    qr_file = "QRs"
    csv_file = "face_recognition_app/alumnos.csv"

    generar_qr(qr_file, codigo)  
    guardar_datos(csv_file, codigo, nombre, carrera) 