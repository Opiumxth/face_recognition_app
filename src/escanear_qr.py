import cv2
from pyzbar.pyzbar import decode

def leer_qr_camara():
        cap = cv2.VideoCapture(0)

        while True:
                ret, frame = cap.read()
                if not ret:
                        break
                imagen_decodeada = decode(frame)

                for img in imagen_decodeada:
                        cap.release()
                        cv2.destroyAllWindows()
                        return img.data.decode('utf-8')

                cv2.imshow("Escanea tu codigo QR!", frame)
                if cv2.waitKey(1) == 27:
                      break

        cap.release()
        cv2.destroyAllWindows()
        return None