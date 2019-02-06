from ..kernel import core_kernel


class Actor:
    def __init__(self, emit_event=None, listen_event=None):
        self.emit_event = emit_event
        self.__emit_callback = None
        core_kernel.register(self, emit_event, listen_event)

    def attach_callback(self, emit_callback):
        self.__emit_callback = emit_callback

    def emit(self, content):
        self.__emit_callback(self.emit_event, content)

    def listen(self, content):
        raise NotImplemented('Listen method not implemented')
