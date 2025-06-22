import cv2
import os
import numpy as np

def cargar_imagenes(folder, image_size=(200, 200)):
    images = []
    labels = []

    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, image_size)
            images.append(img)
            label = os.path.basename(filename).split('_')[0]  # Extrae la etiqueta del nombre del archivo
            labels.append(int(label))  # Convierte la etiqueta a entero

    return images, labels

def entrenar_modelo():
    # Carpeta donde se encuentran las imágenes de entrenamiento
    train_folder = 'faces'

    # Cargar imágenes y etiquetas desde la carpeta
    images, labels = cargar_imagenes(train_folder)

    # Convertir listas a numpy arrays
    images = np.array(images)
    labels = np.array(labels)

    # Crear el reconocedor de rostros basado en Eigenfaces
    model = cv2.face.EigenFaceRecognizer_create()

    # Entrenar el modelo con las imágenes y etiquetas
    model.train(images, labels)

    # Guardar el modelo entrenado
    model.save('eigenfaces_model.xml')

    print("Modelo de reconocimiento facial entrenado y guardado como 'eigenfaces_model.xml'.")

#if __name__ == '__main__':
#    entrenar_modelo()
#    print("Entrenamiento completado.")