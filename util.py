import pygame

class Board:
    """Represents the game board for Tetris."""
    
    UNIT_WIDTH = 9  # Number of units along the width
    UNIT_HEIGHT = 16  # Number of units along the height
    debug = True

    COLORS = {'.' : (0, 0, 0),  # Color for empty cells (Black)
              '■' : (70, 70, 70)}  # Color for filled cells (Gray)

    def __init__(self, screen):
        """Initialize a new game board."""
        # Create a 2D list (UNIT_HEIGHT x UNIT_WIDTH) filled with '.'
        self.board = [["." for _ in range(self.UNIT_WIDTH)] for _ in range(self.UNIT_HEIGHT)]

        self.screen = screen
        self.WIDTH = screen.get_width()
        self.HEIGHT = screen.get_height()

        self.BLOCK_WIDTH = self.WIDTH // self.UNIT_WIDTH
        self.BLOCK_HEIGHT = self.HEIGHT // self.UNIT_HEIGHT

        if self.debug:
            print("Initialized Board")
            # TODO: Add more debug info

    def get_board(self):
        return self.board

    def draw(self):
        print(self)
        # Iterate through each row
        for y, row in enumerate(self.board):
            # Iterate through each cell in the row
            for x, cell in enumerate(row):
                # Determine the (x,y) position on the screen for this block
                rect = pygame.Rect(x * self.BLOCK_WIDTH, y * self.BLOCK_HEIGHT, self.BLOCK_WIDTH-1, self.BLOCK_HEIGHT-1)

                # Draw the block using the appropriate color
                pygame.draw.rect(self.screen, self.COLORS[cell], rect)





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
    print("lame")

    