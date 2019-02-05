from .modules import Module
from ..models import Message


class TerminalInput(Module):
    __name = "Terminal Input"
    __type = 'IO'
    __data_flow = 'IN'

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            in_data = input("$$ ")

            if in_data == "exit":
                return

            message = Message(self.__type, self.__name, self.__data_flow, in_data)
            self.send_message(message)



