import cv2
import dlib

detector = dlib.get_frontal_face_detector()  # detector face frontal
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  # predictor usado

img = cv2.imread('imagens/minhaFoto2.jpg')
resized = cv2.resize(img, (500, 500))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # imagem em escala de cinza



faces = detector(gray)
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

# procurando pelos landmarks
    landmarks = predictor(image=gray, box=face)

# ponto específico
    # x = landmarks.part(27).x  # o ponto 27 é bem no meio dos olhos
    # y = landmarks.part(27).y
# todos os 68 pontos
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y

    # cv2.rectangle(img, (x1, y1), (x2, y2), color=(0, 255, 0))  # desenhando um retângulo
        cv2.circle(img=resized, center=(x, y), radius=2, color=(0, 255, 0), thickness=-1)

cv2.imshow(winname='Face', mat=resized)
cv2.waitKey()
cv2.destroyAllWindows()

