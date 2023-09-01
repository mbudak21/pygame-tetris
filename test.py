import pygame

class board:
    # self.board[y][x] 
    def __init__(self):
        self.board = []
        self.WIDTH, self.HEIGHT = 9, 16


        for row in range(self.HEIGHT):
            self.board.append([])
            for _ in range(self.WIDTH):
                self.board[row].append(None)


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

    