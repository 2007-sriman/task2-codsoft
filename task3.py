import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

print("Press 'q' to quit...")

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    
    if len(faces) > 0:
        text = "Human Found"
        color = (0, 255, 0)
    else:
        text = "No Human Found"
        color = (0, 0, 255)

    
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    
    cv2.imshow('Face Detection - Haar Cascades-codesoft', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
