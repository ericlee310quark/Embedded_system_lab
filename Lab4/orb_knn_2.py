import cv2
import math

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
    #pairs_of_matches = sorted(pairs_of_matches, key=lambda x: (abs(((x[0].distance)**2)-((x[1].distance)**2))))
    print(len(pairs_of_matches))
    # Draw the 25 best pairs of matches.
    
    img_pairs_of_matches = cv2.drawMatchesKnn(
        img0, kp0, img1, kp1, pairs_of_matches[:25], img1,
        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
    
    # Show the pairs of matches.
    cv2.imshow('Before ratio test', img_pairs_of_matches)

    # Apply the ratio test.
    mask_matches = [[0, 0] for i in range(len(pairs_of_matches))]

    # Populate the mask based on David G. Lowe's ratio test.
    for i, (m, n) in enumerate(pairs_of_matches):
        if m.distance < 0.8 * n.distance:
            mask_matches[i] = [1, 0]

    # Draw the best 25 matches.
#    img_matches = cv2.drawMatches(
#        img0, kp0, img1, kp1, matches[:25], img1,
#        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
    img_matches = cv2.drawMatchesKnn(
        img0, kp0, img1, kp1, pairs_of_matches[:25], None,
        singlePointColor=(255, 0, 0),
        matchesMask=mask_matches[:25], flags=0)
    # Show the matches.
    cv2.imshow('After ratio test', img_matches)

    cv2.waitKey()
    cv2.destroyAllWindows()
