import cv2
cap = cv2.VideoCapture("Y2meta.app-video playa corto mp4-(720p60).mp4")

while(True):
  ret, frame = cap.read()

  if ret == False:
    print("El frame está vacío")
    break
  
  cv2.imshow("Mi primer OpenCV", frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()