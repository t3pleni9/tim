class Message:
    def __init__(self, message_type, src, data_flow_direction, content):
        self.content = content
        self.dfd = data_flow_direction
        self.src = src
        self.message_type = message_type

    def __str__(self):
        return self.content + self.message_type + self.src

    def apply(self, func):
        return func(self.content)
