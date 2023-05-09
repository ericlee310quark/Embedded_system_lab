import os.path as path

import cv2


def convert_to_pencil_sketch(rgb_image):
    # TODO: finish this filter
    #result = rgb_image
    img = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    img2 = cv2.GaussianBlur(img,(0,0),cv2.BORDER_DEFAULT)
    
    result = cv2.divide(img, img2, dst=None, scale=256, dtype=None)    

    return result


if __name__ == '__main__':
    img = cv2.imread(path.join('images', 'Lenna.jpg'))
    sketch = convert_to_pencil_sketch(img)

    cv2.imshow("Sketch", sketch)

    cv2.waitKey()
    cv2.destroyAllWindows()
