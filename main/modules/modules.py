from ..kernel import core_kernel


class Module:
    def __init__(self):
        self.callback = None
        core_kernel.subscribe(self)

    def attach_callback(self, callback):
        self.callback = callback

    def send_message(self, message):
        self.callback(message)
