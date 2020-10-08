import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#all code here is based off the tutorials provided

while(1):
    #take each frame
    _, frame = cap.read()
    #print(frame.shape)

    #cup_blue = np.uint8([[[217, 187, 163]]])
    #cup_hsv = cv2.cvtColor(cup_blue, cv2.COLOR_BGR2HSV)
    #print(cup_hsv)
    #convert BGR to HSV
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define range of color in HSV
    #for blue cup (217, 187, 162) in bgr order
    #lower_color = np.array([107, 63, 217])
    lower_color = np.array([185, 50, 50])
    upper_color = np.array([255, 255, 255])
    #lower_color = np.array([110, 50, 50])
    #upper_color = np.array([130, 255, 255])

    #threshold the HSV image to get only the desired colors
    mask = cv2.inRange(frame, lower_color, upper_color)
    
    #bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)
    #cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('res', res)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    #The above code is based off the code from the Changing Colorspaces tutorial provided in the lab document

    img = mask
    #edges = cv2.Canny(img, 100, 200)
    #cv2.imshow('edges', edges)
    #cv2.imshow('img', img)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #ret, thresh = cv2.threshold(img, 127, 255, 0)
    #cv2.imshow('thresh', thresh)
    edges = cv2.Canny(thresh, 100, 200)
    cv2.imshow('edges', edges)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    max_contour_area = 0
    if (len(contours) > 0):
        cnt = contours[0]
        for contour_i in contours:
            if cv2.contourArea(contour_i) > max_contour_area:
                cnt = contour_i

    #hull = cv2.convexHull(cnt)
    #rect = cv2.minAreaRect(cnt)
    #box = cv2.boxPoints(rect)
    #box = np.int0(box)

    x, y, w, h = cv2.boundingRect(cnt)
    im = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    #im = cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
    cv2.imshow('im',  im)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()