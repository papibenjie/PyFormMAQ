from lib.apps import App
from lib.controls import Button

app = App()

btn = Button()
btn.rect.center = App.instance().screen.get_rect().center

app.root.children.append(btn)

app.run()
