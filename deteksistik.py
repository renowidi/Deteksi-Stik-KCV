import cv2

# Mengimport Cascade
stik_cascade = cv2.CascadeClassifier('stik.xml')

# Membuka kamera untuk mengambil video
cap = cv2.VideoCapture(0)

while True:

    # Membaca frame
    _, img = cap.read()

    # Mengubah frame ke warna grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mendeteksi objek pada frame
    stik = stik_cascade.detectMultiScale(gray, 1.1, 4)

    # Menandakan objek dengan memberikan kotak disekitar
    for (x, y, w, h) in stik:

        # Menambahkan teks diatas kotak
        cv2.putText(img, 'Joystick', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (120, 111, 67), 2, cv2.LINE_AA)

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Menampilkan output
    cv2.imshow('Deteksi Stik', img)
    if cv2.waitKey(1) & 0xff == ord('i'):
        break

# Menjalankan tangkapan video
cap.release()
