from lib.constants import Rects, Colors
import pygame
from .base_control import BaseControl
import lib.apps as apps


class Label(BaseControl):
    def __init__(self, rect=Rects.SMALL, font_file="freesansbold.ttf", font_size=24, text="Label", fore_color=Colors.BLACK, back_color=None):
        super(Label, self).__init__("Label")
        self.font_file = font_file
        self.font_size = font_size
        self.text = text
        self.fore_color = fore_color
        self.back_color = back_color
        self.rect = rect
        self.surf = None

    def update(self):
        font = pygame.font.Font(self.font_file, self.font_size)
        self.surf = font.render(self.text, True, self.fore_color, self.back_color)
        self.rect.size = self.surf.get_rect()[-2:]

    def render(self):
        if self.surf is not None and self.rect is not None:
            apps.App.instance().screen.blit(self.surf, self.rect)

    def handle_event(self, event):
        pass
