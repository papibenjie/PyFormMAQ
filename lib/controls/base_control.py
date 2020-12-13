from abc import ABC, abstractmethod


class BaseControl(ABC):
    currentId = 0

    def __init__(self, name):
        super(BaseControl, self).__init__()
        self.name = name
        self.id = BaseControl.currentId
        self.events = {}
        BaseControl.currentId += 1

    def add_event(self, name, default_handler=lambda data: None):
        self.events[name] = [default_handler]

    def call_event(self, name, event_obj):
        for handlers in self.events[name]:
            handlers(event_obj)

    def update_attributes(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass
