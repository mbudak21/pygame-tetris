import pygame
from util import Board

GRID_WIDTH, GRID_HEIGHT = 450, 900
WIDTH, HEIGHT = 750, 1000
FILL_COLOR = (30, 30, 30)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Width, height
        self.running = True

        self.board = Board(pygame.Surface((GRID_WIDTH, GRID_HEIGHT))) # Init board class
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def update(self):
        pass  # Game logic here
    
    def draw(self):
        self.screen.fill(FILL_COLOR)
        # Draw here
        self.screen.blit(self.board.surface, ((WIDTH-GRID_WIDTH)/2, (HEIGHT-GRID_HEIGHT)))
        self.board.draw()
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
