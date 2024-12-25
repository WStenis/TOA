import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TITLE = "TOA"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game States
STATE_MAIN_MENU = "main_menu"
STATE_PLAYING = "playing"
STATE_QUIT = "quit"
game_state = STATE_MAIN_MENU

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Functions for Game States
def draw_main_menu():
    screen.fill(WHITE)
    title_text = font.render("Thrones of Astoria", True, BLACK)
    play_text = small_font.render("Press ENTER to Play", True, GRAY)
    quit_text = small_font.render("Press ESC to Quit", True, GRAY)

    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))
    screen.blit(play_text, (SCREEN_WIDTH // 2 - play_text.get_width() // 2, 300))
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 350))
    pygame.display.flip()

def handle_main_menu_events():
    global game_state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = STATE_QUIT
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Start the game
                game_state = STATE_PLAYING
            elif event.key == pygame.K_ESCAPE:  # Quit the game
                game_state = STATE_QUIT

def play_game():
    global game_state

    # Initialize game objects
    player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    player_speed = 5

    while game_state == STATE_PLAYING:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = STATE_QUIT

        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN]:
            player_pos[1] += player_speed
        if keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed

        # Update game state
        screen.fill(WHITE)

        # Draw player
        pygame.draw.rect(screen, BLACK, (*player_pos, 20, 20))

        pygame.display.flip()
        clock.tick(FPS)

def main():
    global game_state

    while game_state != STATE_QUIT:
        if game_state == STATE_MAIN_MENU:
            draw_main_menu()
            handle_main_menu_events()
        elif game_state == STATE_PLAYING:
            play_game()

    # Cleanup
    pygame.quit()
    sys.exit()

# Entry point
if __name__ == "__main__":
    main()
