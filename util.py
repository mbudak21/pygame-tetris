import pygame

class TetrisBlock:
    def __init__(self, shape, x, y):
        self.shape = shape
        # Hardcoded center values
        self.x = 4 
        self.y = 4
    
    def move(self, dx, dy):
        # TODO: Wall and other shape collision
        self.x += dx
        self.y += dy
    
    def rotate(self):
        # Rotate the block
        pass
    
class Board:
    """Represents the game board for Tetris."""
    
    UNIT_WIDTH = 9  # Number of units along the width
    UNIT_HEIGHT = 16  # Number of units along the height
    debug = True


    GAP_SIZE = 1
    COLORS = {'.' : (0, 0, 0),  # Color for empty cells (Black)
              '■' : (70, 70, 70)}  # Color for filled cells (Gray)

    def __init__(self, surface):
        """Initialize a new game board on the given surface."""
        # Create an empty 2D list (UNIT_HEIGHT x UNIT_WIDTH) filled with '.'
        self.board = [["." for _ in range(self.UNIT_WIDTH)] for _ in range(self.UNIT_HEIGHT)]

        # self.board[0][0] = "■"
        # self.board[1][3] = "■"
        # self.board[3][1] = "■"
        # self.board[1][1] = "■"
        # self.board[2][2] = "■"
        # self.board[3][3] = "■"
        # self.board[4][4] = "■"

        self.surface = surface
        self.WIDTH = surface.get_width()
        self.HEIGHT = surface.get_height()

        self.BLOCK_WIDTH = self.WIDTH // self.UNIT_WIDTH
        self.BLOCK_HEIGHT = self.HEIGHT // self.UNIT_HEIGHT

        if self.debug:
            print("Initialized Board")
            # TODO: Add more debug info

    def get_board(self):
        return self.board

    def draw(self, current_block):
        if self.debug:
            print("Board:")
            print(self)

        self.surface.fill("purple")
        
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                # Determine the (x,y) position on the screen for this block
                rect = pygame.Rect(x * self.BLOCK_WIDTH, y * self.BLOCK_HEIGHT, self.BLOCK_WIDTH-self.GAP_SIZE, self.BLOCK_HEIGHT-self.GAP_SIZE)

                # Draw the block using the appropriate color
                pygame.draw.rect(self.surface, self.COLORS[cell], rect)

        # Draw the current block
        for y, row in enumerate(current_block.shape):
            for x, cell in enumerate(row):
                if cell != ".":
                    # Same logic
                    rect = pygame.Rect(x * self.BLOCK_WIDTH, y * self.BLOCK_HEIGHT, self.BLOCK_WIDTH-self.GAP_SIZE, self.BLOCK_HEIGHT-self.GAP_SIZE)
                    pygame.draw.rect(self.surface, self.COLORS[cell], rect)





    def __str__(self):
        # Initialize an empty list to collect strings
        rows = []
        
        # Iterate through each row in self.board
        for row in self.board:
            # Convert each element in the row to a string, then join them with spaces
            row_str = ' '.join(map(str, row))
            
            # Add the row string to the list
            rows.append(row_str)
        
        # Join all row strings with newlines to form the final string representation
        return '\n'.join(rows)        

if __name__ == "__main__":
    from main import Game
    game = Game()
    game.run()

    