import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.pyrDown(cv2.imread("images/shape.jpg", cv2.IMREAD_UNCHANGED))

    ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                                127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    black = np.zeros_like(img)
    for cnt in contours:
        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        hull = cv2.convexHull(cnt)

        # 2nd argument -1 means we want to draw all contours within the list
        # Last argument is line thickness
        cv2.drawContours(black, [cnt], -1, (0, 255, 0), 2)  # Green
        cv2.drawContours(black, [approx], -1, (255, 255, 0), 2)  # Cyan
        cv2.drawContours(black, [hull], -1, (0, 0, 255), 2)  # Red

    cv2.imshow("Contours", black)
    cv2.waitKey()
    cv2.destroyAllWindows()
