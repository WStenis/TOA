import pygame
from .state_base import GameState

class Gameplay(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.player_pos = [game.screen_width // 2, game.screen_height // 2]
        self.player_speed = 5

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player_pos[1] -= self.player_speed
        if keys[pygame.K_DOWN]:
            self.player_pos[1] += self.player_speed
        if keys[pygame.K_LEFT]:
            self.player_pos[0] -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player_pos[0] += self.player_speed

    def render(self, screen):
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (*self.player_pos, 40, 40))
