from .base_app import BaseApp
from lib.constants import Colors
import lib.controls as ctrl


class App(BaseApp):
    _instance = None

    @staticmethod
    def instance():
        if App._instance is None:
            return App()
        return App._instance

    def __init__(self, size=(800, 600), bg_color=Colors.WHITE, fps=60, ups=100):
        if App._instance is None:
            super(App, self).__init__(size, bg_color, fps, ups)
            self.root = ctrl.Container(self.screen.get_rect(), bg_color)
            App._instance = self
        else:
            raise TypeError("This class is a singleton!")

    def render(self):
        self.root.render()

    def update(self):
        self.root.update()

    def handle_event(self, event):
        self.root.handle_event(event)
