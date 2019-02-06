from .actor import Actor
from ..models import Message, Event


class TerminalInput(Actor):
    __name = "Terminal Input"
    __type = 'IO'
    __data_flow = 'IN'

    def __init__(self):
        super().__init__(Event.INPUT, Event.INIT)

    def listen(self, *args):
        while True:
            in_data = input("$$ ")
            message = Message(self.__type, self.__name, self.__data_flow, in_data)
            self.emit(message)

    @staticmethod
    def init():
        TerminalInput()
