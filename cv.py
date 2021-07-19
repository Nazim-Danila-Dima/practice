import cv2

import pub

if __name__ == '__main__':
    def nothing(*arg):
        pass


    cv2.namedWindow("out_window")
    cap = cv2.VideoCapture("video.mp4")
    pub.start()

    while True:
        flag, img = cap.read()

        height, width = img.shape[:2]
        edge = 10

        try:

            hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

            mask = cv2.inRange(hsv, (0, 160, 20), (122, 255, 255))
            cv2.imshow("mask", mask)

            contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            contours = contours[0]

            if contours:
                cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
                c = max(contours, key=cv2.contourArea)

                left = tuple(c[c[:, :, 0].argmin()][0])
                right = tuple(c[c[:, :, 0].argmax()][0])
                top = tuple(c[c[:, :, 1].argmin()][0])
                bottom = tuple(c[c[:, :, 1].argmax()][0])

                cv2.drawContours(img, [c], -1, (36, 255, 12), 2)
                # cv2.circle(frame, left, 8, (0, 50, 255), -1)
                # cv2.circle(frame, right, 8, (0, 255, 255), -1)
                cv2.circle(img, top, 8, (255, 50, 0), -1)
                cv2.circle(img, bottom, 8, (255, 255, 0), -1)
                cv2.imshow("Contours", img)

                # print('left: {}'.format(left))
                # print('right: {}'.format(right))
                print('top: {}'.format(top))
                print('bottom: {}'.format(bottom))
                pub.publish(pub.connect_mqtt(), top, bottom)

            #cv2.imshow("out_window", img)
        except:
            cap.release()
            raise

        ch = cv2.waitKey(50)
        # для выхода надо нажать esc
        if ch == 27:
            break
    cap.release()
    cv2.destroyAllWindows()