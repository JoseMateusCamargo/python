import cv2
import numpy as np


def circle_HSV2RGB(frame, radius):
    img = np.ones((frame, frame, 3), np.float32)
    ll, cc = np.indices((frame, frame))
    circle = (ll - frame / 2) ** 2 + (cc - frame / 2) ** 2

    arc_tan_ll = (ll.astype(np.float32) - frame / 2)
    arc_tan_cc = (cc.astype(np.float32) - frame / 2)

    hue = np.rad2deg(np.arctan2(arc_tan_ll, arc_tan_cc))
    saturation = (circle.astype(np.float32)) / radius ** 2

    img[:, :, 0] = hue
    img[:, :, 1] = saturation

    img[circle > radius ** 2] = [0, 0, 0]
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

    cv2.imshow("CircleHSV2RGB", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


circle_HSV2RGB(400, 180)
