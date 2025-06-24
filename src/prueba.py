import cv2
import numpy as np

def probar_modelo(codigo):
    # Cargar el modelo LBPH entrenado
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read(f"face_recognition_app/models/modelo_lbph_{codigo}.yml")

    # Inicializar la captura de video desde la cámara
    cap = cv2.VideoCapture(0)

    # Crear un detector de rostros usando Haar cascades
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        # Leer un fotograma de la cámara 
        ret, frame = cap.read()
        if not ret:
            break
    
        # Convertir el fotograma a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Detectar rostros en el fotograma
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    
        for (x, y, w, h) in faces:
            # Extraer la región de interés (el rostro)
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (200, 200))  # Mismo tamaño que durante el entrenamiento
        
            # Predecir usando el modelo LBPH
            label, confidence = model.predict(roi_gray)
            
            # Dibujar un rectángulo alrededor del rostro detectado
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Umbral de confianza (ajustar según tus necesidades)
            # En LBPH, valores bajos de confidence indican mayor similitud
            if confidence < 40:  # Umbral más estricto para LBPH
                cv2.putText(frame, f'Alumno {codigo} Conf: {confidence:.2f}', (x, y-10), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                cv2.putText(frame, 'No reconocido', (x, y-10), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        
        # Mostrar el fotograma
        cv2.imshow('Reconocimiento Facial', frame)
    
        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la captura de video y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()
    
probar_modelo("24200093")