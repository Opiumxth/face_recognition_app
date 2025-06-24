import qrcode
import os
import csv

def generar(qr_file, csv_file):
    codigo = int(input("Ingrese el código del estudiante: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
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
    
    file_exists = os.path.isfile(csv_file)  # Verificar si el archivo ya existe
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        campos = ["codigo", "nombre", "carrera"]
        escritor = csv.DictWriter(file, fieldnames=campos)
        
        # Escribir encabezado solo si el archivo no existe
        if not file_exists:
            escritor.writeheader()
        
        # Guardar los datos del estudiante
        escritor.writerow({
            "codigo": codigo,
            "nombre": nombre,
            "carrera": carrera,
        })
    
#ruta = C:\Users\USUARIO\Desktop\qrs    
qrf = "C:/Users/USUARIO/Desktop/qrs"
csvfile = "C:/Users/USUARIO/Desktop/qrs/base_datos.csv"
if __name__ == '__main__':
    generar(qrf,csvfile)