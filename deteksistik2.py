import cv2  # Mengimport library opencv

stik_cascade = cv2.CascadeClassifier('stik.xml')

cap = cv2.VideoCapture('test7.mp4')

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stik = stik_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in stik:
        cv2.putText(img, 'Joystick', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (120, 111, 67), 3, cv2.LINE_AA)
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

    # Display the output
    cv2.imshow('Deteksi Stik', img)
    if cv2.waitKey(1) & 0xFF == ord('i'):
        break

cap.release()
