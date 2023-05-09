import cv2
import numpy as np

from ssd.classes import CLASSES_90
TRACKED_CLASSES = ["person", "bicycle", "car", "motorcycle"]
BOX_COLOR = (23, 230, 0)
TEXT_COLOR = (255, 255, 255)
INPUT_SIZE = (1920, 1080)


def illustrate_box(image: np.ndarray, box: np.ndarray, caption: str) -> None:
    rows, cols = image.shape[:2]
    points = box.reshape((2, 2)) * np.array([cols, rows])
    p1, p2 = points.astype(np.int32)
    cv2.rectangle(image, tuple(p1), tuple(p2), BOX_COLOR, thickness=4)
    cv2.putText(
        image,
        caption,
        tuple(p1),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        TEXT_COLOR,
        2)

    


def illustrate_detections(objects: np.ndarray, image: np.ndarray) -> np.ndarray:
    # TODO: loop through all objects and draw bounding boxes using illustrate_box()
    # You need to filter the objects, only draw the objects in TRACKED_CLASSES
    for i in objects:
        if i[0]==4:
            Text= TRACKED_CLASSES[3]
        elif i[0]==3:
            Text= TRACKED_CLASSES[2]
        elif i[0]==0:
            Text= TRACKED_CLASSES[1]
        x1=int(i[2]*1920)
        y1=int(i[3]*1080)
        x2=int(i[4]*1920)
        y2=int(i[5]*1080)
        print(i[0],i[1],x1,x2)
        image = cv2.putText(image, Text, (x1,y1), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,TEXT_COLOR,1, cv2.LINE_AA)
        image= cv2.rectangle(image,(x1,y1), (x2,y2),BOX_COLOR,2)
    
    return image


if __name__ == '__main__':
    # Read SSD model
    config = "ssd/ssd_mobilenet_v1_coco_2017_11_17.pbtxt.txt"
    model = "ssd/frozen_inference_graph.pb"
    detector = cv2.dnn.readNetFromTensorflow(model, config)

    # Read input image
    img = cv2.imread('images/street.png')

    # Initialize input
    detector.setInput(
        cv2.dnn.blobFromImage(
            img,
            size=INPUT_SIZE,
            swapRB=True,
            crop=False))

    # Do inference on image
    detections = detector.forward()[0, 0, :, 1:]
    scores = detections[:, 1]
    THRESHOLD = 0.3

    # TODO: remove the object from detections if its score < THRESHOLD
    for i in range(0, len(scores)):
        if scores[i]<THRESHOLD:
            del detections[i]
    # Draw result
    out = illustrate_detections(detections, img)

    cv2.imshow('lab4-4', img)

    cv2.waitKey()
    cv2.destroyAllWindows()
