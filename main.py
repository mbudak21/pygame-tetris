import pygame
from util import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600)) # Width, height
        self.running = True 
    
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
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
