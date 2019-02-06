import sys

from ..models import LanguageProcessor, Event
from .actor import Actor


class LanguageActor(Actor):
    __name = "Language"
    __type = 'IO'
    __data_flow = 'IN-OUT'

    def __init__(self):
        super().__init__(None, Event.INPUT)
        self.__processor = LanguageProcessor.get_instance()

    def listen(self, message):
        speech_class = self.__processor.speech_class(message)
        sys.stderr.write(speech_class + '\n')
        if speech_class == 'Bye':
            sys.stderr.write('Tim signing off\n')
            exit(0)

    @staticmethod
    def init():
        LanguageActor()

