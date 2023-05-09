import cv2
import numpy as np
if __name__ == '__main__':
    img = cv2.imread("images/star.jpg")
    cv2.imshow("original", img)
    img_h = img.shape[0]
    img_w = img.shape[1]
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(img_h)
    print(img_w)
    # TODO: DO the image processing, clean up unwanted background
    #gray_img = cv2.medianBlur(gray_img, 5)
    gray_img = cv2.Canny(gray_img, 210,210)
    x1 = 224
    x2 = 460
    y1 = 197
    y2 = 416
    clean = gray_img
    cv2.imshow("before", clean)
    ret, clean = cv2.threshold(clean,150, 255, cv2.THRESH_BINARY)
    clean = clean[y1:y2,x1:x2]
    clean[146:251,0:48]=0
    cv2.imshow("after", clean)
    
    print(clean.shape[0])
    print(clean.shape[1])

    # Extract contours
    contours, hierarchy = cv2.findContours(clean, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    #clean = clean[10:210,10:209]
    # TODO: Extract the contours from start shape, contours is a list of np.ndarray
    star = contours
    for i in range(len(star)):
        J=np.array([x1,y1])
        star[i]=star[i]+J
    

    img = cv2.drawContours(img, star, -1, (0, 0, 255), 2)  # The contour argument must be a list

    cv2.imshow("lab4-1", img)

    cv2.waitKey()
    cv2.destroyAllWindows()
