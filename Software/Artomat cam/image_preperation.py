import cv2
import numpy as np

min_value = 100
max_value = 200

def on_min_trackbar(value):
    global min_value
    min_value = int(value)


def on_max_trackbar(value):
    global max_value
    max_value = int(value)


def prepare_image(path, mock=False):
    global min_value
    global max_value

    img = cv2.imread(path)
    edges = None

    step = 50

    if not mock:

        cv2.namedWindow("Vision")
        cv2.startWindowThread()
        cv2.createTrackbar("min_value", "Image Edges", min_value, 3000, on_min_trackbar)
        cv2.createTrackbar("max_value", "Image Edges", max_value, 3000, on_max_trackbar)

        confirmed = False
        while not confirmed and cv2.getWindowProperty('Vision', cv2.WND_PROP_VISIBLE) > 0:
            edges = cv2.Canny(img, min_value, max_value)

            cv2.imshow('Vision', np.hstack([img, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)]))

            key = cv2.waitKey(1)

            if key == 105:  # I
                max_value += step

            elif key == 107:  # K
                max_value -= step

            elif key == 119:  # W
                min_value += step

            elif key == 115:  # S
                min_value -= step

            elif key == 13:  # Enter
                confirmed = True

        if not confirmed:
            cv2.destroyWindow("Vision")
            cv2.waitKey(1)
            exit(-1)

    else:
        edges = cv2.Canny(img, min_value, max_value)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    return edges
