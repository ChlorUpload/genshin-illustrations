import cv2
import sys
import os.path


def detect(filename, cascade_file="./utils/datagen1/lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor=1.1,
                                     minNeighbors=4,
                                     minSize=(100, 100))

    return (image, faces)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("usage: anime_face_detect.py <filename>\n")
        sys.exit(-1)

    image, faces = detect(sys.argv[1])

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("AnimeFaceDetect", image)
    cv2.waitKey(0)
