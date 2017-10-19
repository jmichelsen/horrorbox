import logging
import time
from subprocess import call

import constants
from motion_detection import FearsEye
from music import HorrorsEar

log = logging.getLogger(__file__)


class FearItself(object):
    def __init__(self):
        self.ear = HorrorsEar()
        self.eye = FearsEye()

    def begin(self):
        self.ear.begin()
        self.eye.action_methods.append(getattr(self.ear, 'scare'))
        self.eye.action_methods.append(self.fears_shroud)
        self.eye.begin()

    @staticmethod
    def fears_shroud():
        try:
            call(constants.SMOKE_SCRIPT)
            log.info('Running smoke machine')
            time.sleep(constants.SMOKE_DURATION)
            log.info('Stopping smoke machine')
            call(constants.SMOKE_SCRIPT)
        except Exception as e:
            log.error(e)


if __name__ == '__main__':
    FearItself().begin()
