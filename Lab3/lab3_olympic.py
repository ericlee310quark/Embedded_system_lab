import cv2
import numpy as np

if __name__ == '__main__':
    symbol = np.zeros((400, 700, 3), dtype=np.uint8)

    # TODO: change to white background and draw circles in symbol

    symbol[: ,:,:] = 255
    
    
    cv2.circle(symbol, (250, 150), 50, (255, 0, 0), thickness=2)
    cv2.circle(symbol, (350, 150), 50, (0, 0, 0), thickness=2)
    cv2.circle(symbol, (450, 150), 50, (0, 0, 255), thickness=2)
    cv2.circle(symbol, (300, 200), 50, (0, 255, 255), thickness=2)
    cv2.circle(symbol, (400, 200), 50, (0, 255, 0), thickness=2)


    cv2.imshow('olympic symbol', symbol)

    cv2.waitKey()
    cv2.destroyAllWindows()
