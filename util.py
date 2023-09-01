import pygame

class board:
    # self.board[y][x] 
    def __init__(self):
        self.board = []
        self.UNIT_WIDTH, self.UNIT_HEIGHT = 9, 16


        for row in range(self.UNIT_HEIGHT):
            self.board.append([])
            for _ in range(self.UNIT_WIDTH):
                self.board[row].append(".")

    def get_board(self):
        return self.board
    
    def draw(self):
        # TODO: Implement drawing method
        pass

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
    Board = board()
    print(Board)

    