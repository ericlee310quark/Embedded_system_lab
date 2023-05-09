import cv2

if __name__ == '__main__':
    img = cv2.imread("images/star.jpg")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.medianBlur(gray_img, 5)

    # Set minValue and maxValue to filter false positives
    # let minValue == maxValue will be strictly filter out and only leave true positives
    gray_img = cv2.Canny(gray_img, 200, 200)

    cv2.imshow("canny", gray_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
