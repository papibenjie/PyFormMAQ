from abc import ABC, abstractmethod
import pygame


class BaseApp(ABC):
    def __init__(self, size, bg_color, fps, ups):
        super(BaseApp, self).__init__()
        pygame.init()

        self.quit = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(size)
        self.bg_color = bg_color
        self.fps = abs(fps)
        self.ups = abs(ups)

        self.render_dt = 0
        self.update_dt = 0

    def run(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                self.handle_event(event)
            self.tick()

    def tick(self):
        dt = self.clock.tick()
        self.render_dt += dt
        self.update_dt += dt

        if self.fps != 0 and self.render_dt > 1000 / self.fps:
            self.render_dt = 0
            self.screen.fill(self.bg_color)
            self.render()
            pygame.display.flip()

        if self.ups != 0 and self.update_dt > 1000 / self.ups:
            self.update_dt = 0
            self.update()

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass
