class Subscribers:
    def __init__(self):
        self.__emit_subscribers = {}
        self.__listen_subscribers = {}

    def __getitem__(self, event):
        return self.__emit_subscribers[event]

    def add(self, service, emit_event, listen_event):
        self.__add_to_list(self.__emit_subscribers, service, emit_event)
        self.__add_to_list(self.__listen_subscribers, service, listen_event)

    @staticmethod
    def __add_to_list(subscriber_list, service, event):
        if event is None:
            return

        if event not in subscriber_list:
            subscriber_list[event] = []

        subscriber_list[event].append(service)

    def listeners(self, event, content):
        if event not in self.__listen_subscribers:
            return
        for services in  self.__listen_subscribers[event]:
            services.listen(content)
