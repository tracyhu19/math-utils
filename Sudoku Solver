class Solution(object):
  def solveSudoku(self, board):

    #Sudoku variants options
    knight = input("Knight's move? (y/n)\n")
    king = input("King's move? (y/n)\n")
    diagonal = input("Diagonals? (y/n)\n")
    cons = input("Non-consecutive orthogonal squares? (y/n)\n")
    
    def find_blank(board): 
      for x in range(0, 9):
        for y in range(0, 9):
          if board[x][y] == ".":
            return x, y
      return -1, -1
                
    def number_placer(board):
      x, y = find_blank(board)
      if x == -1 and y == -1:
        return True
      for digit in range(1, 10):
        if isValidSudoku(board, x, y, digit):
          board[x][y] = str(digit)
          if number_placer(board):
            return True
        board[x][y] = "."
        
    def isValidSudoku(board, x, y, digit):
      """Checks if board is valid"""
      column = [board[j][y] for j in range(0, 9)]
      if str(digit) in column:
        return False
      if str(digit) in board[x]:
        return False
      box_x, box_y = 3*(x//3), 3*(y//3)
      square = [board[i][j] for i in range(box_x, box_x+3) for j in range(box_y, box_y+3)]
      if str(digit) in square:
        return False
      #Sudoku variant: Knight's move
      if knight == 'y':
        knights = []
        moves = [[-1, 2], [-1, -2], [1, 2], [1, -2], [-2, 1], [-2, -1], [2, -1], [2, 1]]
        for move in moves:
          new_x = x + move[0]
          new_y = y + move[1]
          if new_x >= 0 and new_x < 9 and new_y >= 0 and new_y < 9:
            knights.append(board[new_x][new_y])
        if str(digit) in knights:
          return False
      #Sudoku variant: King's move
      if king == 'y':
        kings = []
        shifts = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for shift in shifts:
          dx = x + shift[0]
          dy = y + shift[1]
          if dx >= 0 and dx < 9 and dy >= 0 and dy < 9:
            kings.append(board[dx][dy])
        if str(digit) in kings:
          return False
      #Sudoku variant: Diagonals
      if diagonal == "y":
        if x == y:
          if str(digit) in [board[i][i] for i in range(0, 9)]:
            return False
        if x == 8-y:
          if str(digit) in [board[j][8-j] for j in range(0, 9)]:
            return False
      #Sudoku variant: non-consecutive orth squares
      if cons == "y":
        moves = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        adj = []
        for move in moves:
          nx = x + move[0]
          ny = y + move[1]
          if nx >= 0 and nx < 9 and ny >= 0 and ny < 9:
            adj.append(board[nx][ny])
        if str(digit - 1) in adj:
          return False
        if str(digit + 1) in adj:
          return False

      return True

    number_placer(board)

board = [["7",".",".","2",".",".",".",".","."], [".",".",".",".",".",".","6",".","."], [".",".",".",".",".",".",".",".","."], [".","3",".",".",".",".",".","8","."], [".",".",".",".",".",".",".",".","."], ["9","5",".",".",".",".",".","4","3"], ["3",".",".",".",".",".",".","9","8"], [".",".","1",".",".",".","2",".","."], ["5",".",".","7",".","8",".",".","4"]]

def struct_sudoku(nums):
  stringy = "-" * 37 + "\n"
  for i in nums:
    for j in i:
      stringy += '| ' + j + " "
    stringy += "|\n"
    stringy += "-" * 37 + "\n"
  return stringy
print(struct_sudoku(board))

sol = Solution()
nums = sol.solveSudoku(board)
  
print(struct_sudoku(board))
