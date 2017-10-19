import os
from logging.config import dictConfig

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MUSIC_PATH = os.path.join(BASE_PATH, 'music/')
SCARE_PATH = os.path.join(BASE_PATH, 'scares/')
SCARE_TRACKS = [os.path.join(SCARE_PATH, track) for track in os.listdir('scares/')]
BACKGROUND_TRACKS = [os.path.join(MUSIC_PATH, track) for track in os.listdir('music/')]
SMOKE_SCRIPT = '/home/pi/horrorbox/smoke.sh'
SMOKE_DURATION = 15

LOGGING = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'verbose': {
            'format': 'fearbox[%(process)d]: %(levelname)s %(name)s[%(module)s] %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'fearbox.log',
            'when': 'midnight',
            'backupCount': 7,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'verbose',
            'address': '/dev/log',
            'facility': 'local2',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logfile', 'syslog'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

dictConfig(LOGGING)
