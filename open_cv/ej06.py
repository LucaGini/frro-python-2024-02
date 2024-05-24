#primitivas: dibujo que puedo hacer sobre un frame

import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    blue = (255,0,0)
    cv2.rectangle(frame,(200,50), (225,125), blue, -1)

    red = (0,0,255)
    cv2.rectangle(frame, (180,200), (210,225), red, 5)

    green = (0, 255, 0)
    cv2.rectangle(frame, (300, 60), (350, 90), green)

    cv2.putText(frame, "Hola Mundo!!", (100,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

    cv2.imshow("Ejemplo de escritura en pantalla", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    #roi = parte que me interesa procesar. En este caso, traslado una parte del frame adonde yo quiero.