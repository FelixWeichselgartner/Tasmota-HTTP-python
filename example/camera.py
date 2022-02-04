from Tasmota.Tasmota import Tasmota
import cv2

ipv4 = "192.168.178.193"
dev = Tasmota(ipv4)
cap = cv2.VideoCapture(dev.get_stream_url())

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
