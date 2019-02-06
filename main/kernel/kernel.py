from .subscribers import Subscribers


class Kernel:
    def __init__(self):
        self.__subscribers = Subscribers()

    def register(self, service_reference, emit_event, listen_event):
        self.__subscribers.add(service_reference, emit_event, listen_event)
        service_reference.attach_callback(self.emit_event)

    def emit_event(self, event, message):
        self.__subscribers.listeners(event, message)


core_kernel = Kernel()
