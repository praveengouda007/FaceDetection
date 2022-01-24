import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('color', frame)
    cv2.imshow('black/white', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):    # press q to close webcam
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()