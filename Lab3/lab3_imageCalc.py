import os.path as path

import cv2

if __name__ == '__main__':
    crazydog = cv2.imread(path.join('images', 'crazydog.jpg'))
    puipui = cv2.imread(path.join('images', 'puipui.jpg'))

    #crazydog =cv2.cvtColor(crazydog, cv2.COLOR_BGR2BGRA)

    crazydog2 = crazydog.copy()
    puipui2 = cv2.flip(puipui,1)
    #puipui2 =cv2.cvtColor(puipui2, cv2.COLOR_BGR2BGRA)
    puipui2 = cv2.resize(puipui2, dsize=(210,180))
    
    #puipui2 = cv2.resize(puipui, dsize=(640,360))
    #crazydog2[:,:,:4] = 255
    #crazydog2[160:340,270:590,:] = puipui2
    crazydog2[30:210,220:430,:] = puipui2
    #crazydog2[:,:,3] = 255
    
   
    
    #cv2.imshow('result3', puipui)
    #cv2.imshow('result2', crazydog2)

    print(crazydog.shape)
    print(puipui.shape)

    # TODO: merge two images
    
    
    #puipui2 = cv2.resize(puipui2, dsize=None, fx=0.5, fy=0.5)
    print(puipui2.shape)
    crazydog = cv2.addWeighted(crazydog, 0.5, crazydog2, 0.5, 0)


    cv2.imshow('result', crazydog)

    cv2.waitKey()
    cv2.destroyAllWindows()
