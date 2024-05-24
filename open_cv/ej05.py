import cv2

captura = cv2.VideoCapture(0) #capturar video
salida = cv2.VideoWriter('videoSalida.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480)) #genera el video, "lo escribe"

while (captura.isOpened()):
    ret, imagen = captura.read() #cuando hace el capture devuelve dos cosas. El frame, y un booleano de si hay o no frame. El ret es el booleano
    if ret == True:
        cv2.imshow('video', imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: break
captura.release()
salida.release()
cv2.destroyAllWindows()