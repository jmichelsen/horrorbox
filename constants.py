import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MUSIC_PATH = os.path.join(BASE_PATH, 'music/')
SCARE_PATH = os.path.join(BASE_PATH, 'scares/')
SCARE_TRACKS = [os.path.join(SCARE_PATH, track) for track in os.listdir('scares/')]
BACKGROUND_TRACKS = [os.path.join(MUSIC_PATH, track) for track in os.listdir('music/')]
