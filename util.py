import pygame
import random

class TetrisBlock:
    O_BLOCK = [
        ["■", "■"],
        ["■", "■"]
    ]
    I_BLOCK = [
        ["■", "■", "■", "■"],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]
    S_BLOCK = [
        [".", "■", "■"],
        ["■", "■", "."],
        [".", ".", "."]
    ]
    Z_BLOCK = [
        ["■", "■", "."],
        [".", "■", "■"],
        [".", ".", "."]
    ]
    L_BLOCK = [
        ["■", ".", "."],
        ["■", "■", "■"],
        [".", ".", "."]
    ]
    J_BLOCK = [
        [".", ".", "■"],
        ["■", "■", "■"],
        [".", ".", "."]
    ]
    T_BLOCK = [
        [".", "■", "."],
        ["■", "■", "■"],
        [".", ".", "."]
    ]
    # Combine all the shapes into a list for easy access
    all_shapes = [O_BLOCK, I_BLOCK, S_BLOCK, Z_BLOCK, L_BLOCK, J_BLOCK, T_BLOCK]

    def __init__(self):
        self.shape=random.choice(self.all_shapes)
        # self.shape=self.all_shapes[0]

        self.depth, self.width = self.get_size()

        # Starting position
        self.x = (Board.UNIT_WIDTH // 2) - self.width//2
        self.y = 0

        print(self.x)



    def get_size(self):
        depth = 0
        width = 0
        for y, row in enumerate(self.shape):
            for x in range(len(row)):
                if row[x] != ".": # Found shape at (x, y)
                    if depth < y+1:
                        depth = y+1
                    if width < x+1:
                        width = x+1
        return depth, width

    def move_left(self):
        # Move the block left
        self.x -= 1
        if self.x < 0:
            self.x = 0
    
    def move_right(self):
        # Move the block right
        if self.x + self.width+1 > Board.UNIT_WIDTH:
            pass
        else:
            self.x += 1

    def move_down(self):
        # Move the block down
        if self.y + self.depth+1 > Board.UNIT_HEIGHT:
            pass
        else:
            self.y += 1
        # Drop the block if it's at the bottom
    
    def drop(self):
        """Saves the block to the boards matrix."""
        pass

    
    def rotate(self):
        # Rotate the block
        pass

    def __str__(self):
        # Initialize an empty list to collect strings
        rows = []
        
        # Iterate through each row in self.board
        for row in self.shape:
            # Convert each element in the row to a string, then join them with spaces
            row_str = ' '.join(map(str, row))
            
            # Add the row string to the list
            rows.append(row_str)
        
        # Join all row strings with newlines to form the final string representation
        return '\n'.join(rows)
    
class Board:
    """Represents the game board for Tetris."""
    
    UNIT_WIDTH = 9  # Number of units along the width
    UNIT_HEIGHT = 16  # Number of units along the height
    debug = False


    GAP_SIZE = 1
    COLORS = {'.' : (0, 0, 0),  # Color for empty cells (Black)
              '■' : (70, 70, 70)}  # Color for filled cells (Gray)

    def __init__(self, surface):
        """Initialize a new game board on the given surface."""
        # Create an empty 2D list (UNIT_HEIGHT x UNIT_WIDTH) filled with '.'
        self.board = [["." for _ in range(self.UNIT_WIDTH)] for _ in range(self.UNIT_HEIGHT)]

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
    
    def merge_with_board(self, shape):
        pass

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
                    rect = pygame.Rect((x + current_block.x) * self.BLOCK_WIDTH, (y + current_block.y) * self.BLOCK_HEIGHT, self.BLOCK_WIDTH-self.GAP_SIZE, self.BLOCK_HEIGHT-self.GAP_SIZE)
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
    Game().run()

    # shape = TetrisBlock()
    # print(shape)
    # print(shape.get_size())

    