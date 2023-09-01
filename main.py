import pygame
from util import Board

WIDTH, HEIGHT = 450, 900


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Width, height
        self.running = True

        self.board = Board() # Init board class
    
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
        self.screen.fill("purple")
        # Draw here
        self.board.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
