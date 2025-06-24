import cv2
import numpy as np

def verificar_rostro():
    #Aqui se carga el modelo entrenado
    model = cv2.face.EigenFaceRecognizer_create()
    model.read('eigenfaces_model.xml')

    #Inicia a capturar video desde la camara
    cap = cv2.VideoCapture(0)

    #Usa el Haar Cascades para detectar los rostros
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        #Lee los fotogramas de la camara, ret se usa como bandera para verificar que exista una camara
        ret, frame = cap.read()
        if not ret:
            break

        #Convertir el fotograma a escala de grises en tiempo real para usar el Haar Cascade
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Detecta los rostros ya con cada frame en escale de grises
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (100, 100))

        for (x, y, w, h) in faces:
            #Extrae la parte de los rostros nada mas
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (200, 200))

            #Se intenta predecir de quien(codigo) es el rostro
            codigo, confianza = model.predict(roi_gray)

            #Dibujar un rectagulo alrededor del rostro detectado en el momento
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            #Muestra el codigo y el nivel de confianza en el fotograma
            cv2.putText(frame, f'Codigo: {codigo}, Conf: {confianza:.2f}', (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 0, 0), 2)

            if confianza < ... :
                print(f"Rostro reconocido correctamente | Codigo: {codigo}")
                cap.release()
                cv2.destroyAllWindows()
                return codigo

        #MUestra el fotograma actualizado
        cv2.imshow('Video', frame)

    cap.release()
    cv2.destroyAllWindows()
    return None