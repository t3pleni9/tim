import sys


class Kernel:
    def __init__(self):
        self.__message_queue = []

    def subscribe(self, service_reference):
        service_reference.attach_callback(self.__attach_message)

    def __attach_message(self, message):
        self.__message_queue.append(message)
        sys.stderr.write(str(message))


core_kernel = Kernel()
