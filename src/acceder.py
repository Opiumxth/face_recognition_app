from escanear_qr import leer_qr_camara
from verificar_codigo_en_csv import verificar_codigo_csv
from acceder_rostro import verificar_rostro

def ejecutar_acceso():
        #Leer el codigo QR
        codigo_qr = leer_qr_camara()
        if not codigo_qr:
                print("No se encontro codigo qr")
                return

        #Verificar el codigo QR
        info_alumno = verificar_codigo_csv()
        if not info_alumno:
                print("Codigo no encontrado en la case de datos")
                return

        #Abrir la camara y con el nivel de confianza en cierto punto cerrar la camara (posible implementacion: timeout)
        codigo_rostro = verificar_rostro():
        if codigo_rostro is None:
                print("No se pudo reconocer el rostro")
                return

        #Abrir la camara y con el nivel de confianza en cierto punto cerrar la camara (posiblemente un timeout)
        if str(codigo_rostro) == codigo_qr:
                print("Acceso concedido, Bienvendido, ", info_alumno["nombre"])
        else:
                print("El rostro no coincide con el codigo QR")