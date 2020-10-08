import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#All code here is based off the tutorials, but moreso from the Determining dominant color article

def find_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0
    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
        startX = endX

    return bar

cap = cv2.VideoCapture(0)
#d_rectangle = np.zeros((240, 320, 3), dtype = np.uint8)
#print(d_rectangle.shape)
while(1):
    _, frame = cap.read()
    d_rectangle = np.zeros((240, 320, 3), dtype = np.uint8)
    #cv2.imshow('frame', frame)
    for i in range(len(d_rectangle)):
        for j in range(len(d_rectangle[i])):
            d_rectangle[i][j] = frame[i+120][j+160]
    #cv2.imshow('d_rectangle', d_rectangle)
    x = 160
    y = 120
    w = 320
    h = 240
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    d_rectangle = cv2.cvtColor(d_rectangle, cv2.COLOR_BGR2RGB)

    d_rectangle = d_rectangle.reshape((d_rectangle.shape[0] * d_rectangle.shape[1], 3))
    clt = KMeans(n_clusters = 3)
    clt.fit(d_rectangle)

    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)

    k = cv2.waitKey(1) & 0xFF
    if k == 97:
        plt.axis("off")
        plt.imshow(bar)
        plt.show()
        #plt.clf()
    elif k == 27:
        break

cv2.destroyAllWindows()