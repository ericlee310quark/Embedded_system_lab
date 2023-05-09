import cv2

if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier(
        './cascades/haarcascade_frontalface_default.xml')

    #eyes_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')

    # TODO: change to faces_2.jpg and adjust parameters
    img = cv2.imread('images/faces_2.jpg')
    img = cv2.resize(img, dsize=None, fx=0.8, fy=0.8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.001, 250)
    #eyes = eyes_cascade.detectMultiScale(gray, 1.2, 9)
    for (x, y, w, h) in faces:
        if w<45 and h<45:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    #for (x, y, w, h) in eyes:
    #    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('lab4-2', img)

    cv2.waitKey()
    cv2.destroyAllWindows()
