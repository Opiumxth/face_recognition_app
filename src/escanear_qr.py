import cv2
from pyzbar.pyzbar import decode

def leer_qr_camara():
        cap = cv2.VideoCapture(0)

        while True:
                ret, frame = cap.read()
                if not ret:
                        break

                imagen_decodeada = decode(frame)

                if imagen_decodeada:
                        codigo_qr = imagen_decodeada[0].data.decode('utf-8')
                        break

                cv2.imshow("Escanea tu codigo QR", frame)

                #Presiona la tecla esc para salir
                if cv2.waitKey(1) == 27:
                        codigo_qr = None
                        break

        cap.release()
        cv2.destroyAllWindows()
        return codigo_qr