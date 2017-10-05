from motion_detection import FearsEye
from music import HorrorsEar


class FearItself(object):
    def __init__(self):
        self.ear = HorrorsEar()
        self.eye = FearsEye()

    def begin(self):
        self.ear.begin()
        self.eye.action_method = getattr(self.ear, 'scare')
        self.eye.begin()


if __name__ == '__main__':
    FearItself().begin()
