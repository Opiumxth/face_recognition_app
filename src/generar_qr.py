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

def guardar_datos_en_csv(csv_file, codigo, nombre, carrera):

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

if __name__ == '__main__':
    qr_file = "C:/Users/USUARIO/Desktop/qrs"  
    csv_file = "C:/Users/USUARIO/Desktop/Repo_id/face_recognition_app/alumnos.csv"

    codigo = int(input("Ingrese el código del estudiante: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")

    generar_qr(qr_file, codigo)  # Genera el código QR
    guardar_datos_en_csv(csv_file, codigo, nombre, carrera)  # Guarda los datos en el CSV