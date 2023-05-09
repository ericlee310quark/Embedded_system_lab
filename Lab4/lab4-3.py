import cv2

if __name__ == '__main__':
    img0 = cv2.imread('images/book_0.JPG',
                      cv2.IMREAD_GRAYSCALE)
    img1 = cv2.imread('images/book_1.JPG',
                      cv2.IMREAD_GRAYSCALE)

    # TODO: Perform SIFT feature detection and description.
    sift = cv2.SIFT_create()
    kp0, des0 = sift.detectAndCompute(img0, None)
    kp1, des1 = sift.detectAndCompute(img1, None)

    # TODO: Define FLANN-based matching parameters.
    
    index = dict(algorithm=1, trees =5)
    search = dict(checks=50)
    flan = cv2.FlannBasedMatcher(index, search)

    
    # TODO: Perform FLANN-based matching.
    matches = flan.knnMatch(des0,des1, k=2)
    # Prepare an empty mask to draw good matches.
    mask_matches = [[0, 0] for i in range(len(matches))]

    # Populate the mask based on David G. Lowe's ratio test.
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7 * n.distance:
            mask_matches[i] = [1, 0]

    
    # TODO: Draw the matches that passed the ratio test.
  
    img_matches = cv2.drawMatchesKnn(img0, kp0, img1,kp1,matches,img1, matchesMask = mask_matches, 
                                    flags=0,    #flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS,
                                    matchColor=(0, 255, 0),
                                    singlePointColor=(255, 0, 0))

    # Show the matches.
    cv2.imshow('lab4-3', img_matches)

    cv2.waitKey()
    cv2.destroyAllWindows()
