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

    def drop_to_bottom(self):
        self.y = Board.UNIT_HEIGHT - self.depth

    
    def rotate(self):
        # Transpose the block (swap rows with columns)
        transposed = list(zip(*self.shape))

        # Reverse each row to get the rotated block
        self.shape = [list(reversed(row)) for row in transposed]        

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
    debug = True


    GAP_SIZE = 1
    COLORS = {'.' : (0, 0, 0),  # Color for empty cells (Black)
              '■' : (70, 70, 70)}  # Color for filled cells (Gray)
    COLORS2 = {'.' : (70, 10, 10),
              '■' : (120, 70, 70)}

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
    
    def merge_with_board(self, block):
        for y, row in enumerate(block.shape):
            for x, cell in enumerate(row):
                if cell != ".":
                    self.board[block.y + y][block.x + x] = cell
    
    def check_block_collision(self, block):
        """
        Checks the collision
        returns True if there is a collision
        """
        # unpack and check overlaps
        for y, row in enumerate(block.shape):
            for x, cell in enumerate(row):
                try:
                    if cell != "." and self.board[block.y + y][block.x + x] != ".":
                        return True # Shape Collision
                except IndexError: 
                    return True # Wall Collision
        return False

    def check_floor_collision(self, block):
        pass

    def create_empty_row(self):
        return ["."] * self.UNIT_WIDTH

    def check_full_rows(self):  # Checks all rows
        full_rows = []
        for i, row in enumerate(self.get_board()):
            if not ("." in row):
                full_rows.append(i)
                if self.debug:
                    print(f"Full row: {i}")
        return full_rows

    def shift_down(self, full_rows):
        for row_index in reversed(full_rows):
            del self.board[row_index]  # Remove the full row
            self.board.insert(0, self.create_empty_row())  # Add an empty row at the top

    def draw(self, current_block):
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
                if True: # cell != ".":
                    # Same logic
                    rect = pygame.Rect((x + current_block.x) * self.BLOCK_WIDTH, (y + current_block.y) * self.BLOCK_HEIGHT, self.BLOCK_WIDTH-self.GAP_SIZE, self.BLOCK_HEIGHT-self.GAP_SIZE)
                    pygame.draw.rect(self.surface, self.COLORS2[cell], rect)

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

    