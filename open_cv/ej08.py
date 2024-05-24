import time
import numpy as np
import cv2

camara = cv2.VideoCapture(".mp4") #Hay que descargar un video. No puedo subirlo a git por tamaño excesivo

#Inicializamos el primer frame no vacio. Nos servirá para obtener el fondo
fondo = None

#Recorremos todos los frames
while True:
    #obtenemos el frame
    (grabbed, frame) = camara.read()

    #Si hemos llegado al final del video salimos
    if not grabbed:
        break

    # Convertimos a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Aplicamos suavizado para eliminar ruido
    gris = cv2.GaussianBlur(gris, (21,21),0)

    #Si todavia no hemos obtenido el fondo, lo obtenemos. Será el primer frame que obtengamos
    if fondo is None:
        fondo = gris
        continue

    #Calculo de la diferencia entre el fondo y el frame actual
    resta = cv2.absdiff(fondo, gris)

    #Aplicamos un umbral
    umbral = cv2.threshold(resta, 25, 255, cv2.THRESH_BINARY)[1]

    #Dilatamos el umbral para tapar agujeros
    umbral = cv2.dilate(umbral, None, iterations=2)

    #Copiamos el umbral para detectar los contornos
    contornosimg = umbral.copy()

    #Buscamos contorno en la imagen
    contornos, hierarchy = cv2.findContours(contornosimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Recorremos todos los contornos encontrados
    for c in contornos:
        #Eliminamos los contornos mas pequeños
        if cv2.contourArea(c) < 500:
            continue

        #Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
        (x,y,w,h) = cv2.boundingRect(c)

        #Dibujamos el rectángulo del bounds
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255,0), 2)

    #Mostramos las imagenes de la cámara, el umbral y la resta
    cv2.imshow('Camara', frame)
    cv2.imshow('Umbral', umbral)
    cv2.imshow('Resta', resta)
    cv2.imshow('Contornos', contornosimg)

    #capturamos tecla para salir
    key = cv2.waitKey(1) & 0xFF


    #Tiempo de espera para que se vea bien
    time.sleep(0.015)
    #Si han pulsado la tecla s salimos
    if key == ord('s'):
        break

#Liberamos la camara y cerramos todas las ventanas
camara.release()
cv2.destroyAllWindows()
