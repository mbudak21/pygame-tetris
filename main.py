import pygame
from util import Board, TetrisBlock

# Constants
GRID_WIDTH, GRID_HEIGHT = 450, 900
WIDTH, HEIGHT = 750, 1000
FILL_COLOR = (30, 30, 30)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Screen
        self.running = True
        

        self.board = Board(pygame.Surface((GRID_WIDTH, GRID_HEIGHT))) # Init board class
        self.current_shape = TetrisBlock()
    
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
                if keys[pygame.K_LEFT]:
                    self.current_shape.move_left()
                if keys[pygame.K_RIGHT]:
                    self.current_shape.move_right()
                if keys[pygame.K_DOWN]:
                    self.current_shape.move_down()
                if keys[pygame.K_UP]:
                    self.current_shape.rotate()
                if keys[pygame.K_SPACE]:
                    # Merge and reset the current_shape
                    self.board.merge_with_board(self.current_shape)
                    self.current_shape = TetrisBlock()
                
    def update(self):
        pass  # Game logic here
    
    def draw(self):
        self.screen.fill(FILL_COLOR)
        # Draw here
        self.screen.blit(self.board.surface, ((WIDTH-GRID_WIDTH)/2, (HEIGHT-GRID_HEIGHT)))
        self.board.draw(self.current_shape)
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
