import pygame
from .state_base import GameState

class CreateCharacter(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Start games
                    self.game.change_state(self.game.gameplay_state)

    def save_character(self, events):
        pass

    def render(self, screen):
        screen.fill((255, 255, 255))
        title = self.font.render("Thrones of Astoria", True, (0, 0, 0))
        play = self.small_font.render("Press ENTER to Play", True, (100, 100, 100))

        screen.blit(title, (self.game.screen_width // 2 - title.get_width() // 2, 100))
        screen.blit(play, (self.game.screen_width // 2 - play.get_width() // 2, 150))