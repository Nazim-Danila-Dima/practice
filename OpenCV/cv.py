import cv2

import cv_pub


def nothing(*arg):
    pass


def run():
    frame = cv2.imread("1.jpg")
    cv2.imshow("frame", frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    mask = cv2.inRange(hsv, (0, 160, 20), (122, 255, 255))
    cv2.imshow("mask", mask)

    contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = contours[0]

    if contours:
        c = max(contours, key=cv2.contourArea)

        left = tuple(c[c[:, :, 0].argmin()][0])
        right = tuple(c[c[:, :, 0].argmax()][0])
        top = tuple(c[c[:, :, 1].argmin()][0])
        bottom = tuple(c[c[:, :, 1].argmax()][0])

        print('left: {}'.format(left))
        print(left[0])
        print('right: {}'.format(right))
        print('top: {}'.format(top))
        print('bottom: {}'.format(bottom))
        cv_pub.publish(cv_pub.connect_mqtt(), top, bottom)

    cv2.destroyAllWindows()

run()


