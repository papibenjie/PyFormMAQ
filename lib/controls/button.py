from lib.controls.base_control import BaseControl
from lib.controls import Label, Container
from lib.constants import Colors, Rects


class Button(BaseControl):
    def __init__(self, rect=Rects.SMALL, fit_content=False, back_color=Colors.WHITESMOKE, fore_color=Colors.BLACK, font_file="freesansbold.ttf", font_size=24, text="Button", hover_back_color=Colors.GRAY, hover_fore_color=Colors.WHITE):
        super(Button, self).__init__("Button")
        self.rect = rect
        self.font_file = font_file
        self.font_size = font_size
        self.text = text

        self.hover_back_color = hover_back_color
        self.hover_fore_color = hover_fore_color
        self.not_hover_fore_color = fore_color
        self.not_hover_back_color = back_color

        self.container = Container(self.rect, self.not_hover_back_color)
        self.label = Label(self.rect.copy() if not fit_content else self.rect, self.font_file, self.font_size, self.text, self.not_hover_fore_color, None)
        self.container.children.append(self.label)

        self.container.events["on_click_hold"].append(self._on_click)

    def update(self):
        hovered = self.container.hovered
        self.container.update_attributes(rect=self.rect.copy(), back_color=(255, 0, 0) if hovered else self.not_hover_back_color)
        self.label.update_attributes(font_file=self.font_file, font_size=self.font_size, text=self.text, fore_color=self.hover_fore_color if hovered else self.not_hover_fore_color)
        self.label.rect.center = self.container.rect.center
        self.container.update()

    def render(self):
        self.container.render()

    def handle_event(self, event):
        self.container.handle_event(event)

    def _on_click(self, event):
        print("CLICK333")
