from lib.constants import Colors, Rects
import pygame
import lib.apps as apps
from .base_control import BaseControl


class Container(BaseControl):
    def __init__(self, rect=Rects.LARGE, back_color=Colors.TRANSPARENT):
        super(Container, self).__init__("Container")
        self.rect = rect
        self.back_color = back_color
        self.children = []
        self.hovered = False

        self.add_event("on_hover", self._on_hover)
        self.add_event("on_not_hover", self._on_not_hover)
        self.add_event("on_mouse_enter")
        self.add_event("on_mouse_leave")
        self.add_event("on_click")
        self.add_event("on_click_hold")

    def update(self):
        for child in self.children:
            child.update()

    def render(self):
        surf = pygame.Surface(self.rect.size)
        surf.fill(self.back_color)
        apps.App.instance().screen.blit(surf, self.rect.topleft)
        for child in self.children:
            child.render()

    def handle_event(self, event):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.call_event("on_hover", event)
        else:
            self.call_event("on_not_hover", event)
        for child in self.children:
            child.handle_event(event)

    # EVENTS
    def _on_hover(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(321)
            self.call_event("on_click_hold", event)
        if not self.hovered:
            self.hovered = True
            self.call_event("on_mouse_enter", event)

    def _on_not_hover(self, event):
        if self.hovered:
            self.hovered = False
            self.call_event("on_mouse_leave", event)
