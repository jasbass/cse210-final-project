from game.actions.action import Action
from game import constants

class CheckBackgroundAudioAction(Action):
    def __init__(self, audio_service) -> None:
        self._audio_service = audio_service

    def execute(self, cast):
        
        if not self._audio_service.check_sound_playing(constants.SOUND_BACKGROUND):
            self._audio_service.play_sound(constants.SOUND_BACKGROUND)
