import logging
import random
import time

import vlc

import constants

log = logging.getLogger(__file__)


class HorrorsEar(object):
    def __init__(self):
        self.background_instance = vlc.Instance()
        self.background_tracks = self.background_instance.media_list_new()
        self.background_player = self.background_instance.media_list_player_new()
        self.scare_player = vlc.MediaPlayer

    def begin(self):
        [self.background_tracks.add_media(self.background_instance.media_new(track))
            for track in constants.BACKGROUND_TRACKS]
        self.background_player.set_media_list(self.background_tracks)
        self.background_player.set_playback_mode(vlc.PlaybackMode.loop)
        self.background_player.play()

    def scare(self):
        track = random.choice(constants.SCARE_TRACKS)
        log.info('playing scare: {}'.format(track))
        player = self.scare_player(track)
        player.play()
        time.sleep(1)
        while player.is_playing():
            continue
        player.release()

    def end(self):
        self.background_player.stop()
        self.background_instance.release()
        self.background_player.release()
