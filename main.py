import pygame
from states.main_menu import MainMenu
from states.gameplay import Gameplay

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Open World RPG")

        self.clock = pygame.time.Clock()
        self.running = True

        # States
        self.main_menu_state = MainMenu(self)
        self.gameplay_state = Gameplay(self)
        self.current_state = self.main_menu_state

    def change_state(self, new_state):
        self.current_state = new_state

    def run(self):
        while self.running:
            events = pygame.event.get()
            self.current_state.handle_events(events)
            self.current_state.update()
            self.current_state.render(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
