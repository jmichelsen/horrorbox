import logging
import time

import cv2
import imutils

log = logging.getLogger(__file__)


class FearsEye(object):
    def __init__(self):
        self.camera = cv2.VideoCapture(-1)
        self.min_area = 500
        self.first_frame = None
        self.action_methods = list()
        time.sleep(.2)

    def begin(self):
        while True:
            try:
                success, frame = self.camera.read()
                if not success:
                    log.info('could not read camera')
                    break

                gray_frame = self._get_generic_frame(frame)

                if self.first_frame is None:
                    self.first_frame = gray_frame
                    continue

                frame_delta = cv2.absdiff(self.first_frame, gray_frame)
                threshold = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

                threshold = cv2.dilate(threshold, None, iterations=2)
                (_, contours, _) = cv2.findContours(
                    threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    if cv2.contourArea(contour) < self.min_area:
                        continue
                    for action in self.action_methods:
                        action()
                    time.sleep(15)
            except KeyboardInterrupt:
                break
            except Exception as e:
                log.info(e.message)
                break

    def end(self):
        self.camera.release()

    @staticmethod
    def _get_generic_frame(frame):
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.GaussianBlur(gray, (21, 21), 0)
