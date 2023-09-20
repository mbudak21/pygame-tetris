import pygame
from util import Board, TetrisBlock

# Constants
GRID_WIDTH, GRID_HEIGHT = 450, 900
WIDTH, HEIGHT = 750, 1000
FILL_COLOR = (30, 30, 30)
AUTOFALL_EVENT = pygame.USEREVENT + 1
FALL_TIME = 200 # in miliseconds, TODO: Level system

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Screen
        self.running = True

        self.board = Board(pygame.Surface((GRID_WIDTH, GRID_HEIGHT))) # Init board class

        pygame.time.set_timer(AUTOFALL_EVENT, 500)
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
    
    def handle_events(self):
        """Handles events and keypress actions"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:  # Handle keypresses here
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
                    self.running = False
                if keys[pygame.K_LEFT]:
                    self.board.move_current_shape(left=True)
                if keys[pygame.K_RIGHT]:
                    self.board.move_current_shape(right=True)
                if keys[pygame.K_DOWN]:
                    self.board.move_current_shape(down=True)
                if keys[pygame.K_UP]:
                    pass
                if keys[pygame.K_SPACE]:
                    pass
                if keys[pygame.K_d]:
                    self.board.current_shape.drop_to_bottom()
            elif event.type == AUTOFALL_EVENT:
                self.board.current_shape.move_down()
        print(self.board.check_current_shape_collision())

    def update(self):
        self.board.shift_down(self.board.check_full_rows())

    
    def draw(self):
        self.screen.fill(FILL_COLOR)
        # Draw here
        self.screen.blit(self.board.surface, ((WIDTH-GRID_WIDTH)/2, (HEIGHT-GRID_HEIGHT)))
        self.board.draw()
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
