import cv2

if __name__ == '__main__':
    # Load the images.
    img0 = cv2.imread('images/book_0.JPG')#,cv2.IMREAD_GRAYSCALE)
    img1 = cv2.imread('images/book_1.JPG')#,cv2.IMREAD_GRAYSCALE)

    # Perform ORB feature detection and description.
    orb = cv2.SIFT_create()
    kp0, des0 = orb.detectAndCompute(img0, None)
    kp1, des1 = orb.detectAndCompute(img1, None)

    # Perform brute-force KNN matching.
    bf = cv2.BFMatcher()#cv2.NORM_HAMMING, crossCheck=False)
    pairs_of_matches = bf.knnMatch(des0, des1, k=2)

    # Sort the pairs of matches by distance.
    pairs_of_matches = sorted(pairs_of_matches, key=lambda x: x[0].distance)
    print(len(pairs_of_matches))
    # Draw the 25 best pairs of matches.
    img_pairs_of_matches = cv2.drawMatchesKnn(
        img0, kp0, img1, kp1, pairs_of_matches[:25], img1,
        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
    
    # Show the pairs of matches.
    cv2.imshow('Before ratio test', img_pairs_of_matches)

    # Apply the ratio test.
    matches = [x[0] for x in pairs_of_matches
               if len(x) > 1 and x[0].distance < 0.8 * x[1].distance]
    #matches = [x[0] for x in pairs_of_matches
    #        if len(x) > 1 and (x[0].distance < 0.8 * x[1].distance or x[0].distance > 1.2 * x[1].distance)]

 


    # Draw the best 25 matches.
    img_matches = cv2.drawMatches(
       img0, kp0, img1, kp1, matches[:25], img1,
       None,
        singlePointColor=(255, 0, 0),
        flags=0
       )#flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

    # Show the matches.
    cv2.imshow('After ratio test', img_matches)

    cv2.waitKey()
    cv2.destroyAllWindows()
