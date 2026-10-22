import random

class Sudoku:
  def __init__(self):
    self.sudoku_map: list[list[int]] = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    self.playable_sudoku_map = None
  def generate_map_vals(self) -> None:
    row_idx = 0
    col_idx = 0
    history = {}

    while row_idx < 9:
      pos = (row_idx, col_idx)

      if pos not in history:
        history[pos] = set()

      placed = False
      numbers = list(range(1, 10))
      random.shuffle(numbers)

      for num in numbers:
        if num not in history[pos]:
          history[pos].add(num)
          if self.is_valid(num=num, col_idx=col_idx, row_idx=row_idx):
            self.sudoku_map[row_idx][col_idx] = num
            placed = True
            break

      if placed:
        col_idx += 1
        if col_idx >= 9:
          row_idx += 1
          col_idx = 0
      else:
        history[pos] = set()
        self.sudoku_map[row_idx][col_idx] = 0
        col_idx -= 1
        if col_idx < 0:
          col_idx = 8
          row_idx -= 1
    self.playable_sudoku_map = self.sudoku_map

  def horizont_checker(self, num: int, row_idx: int) -> bool:
    return num in self.sudoku_map[row_idx]

  def vertical_checker(self, num: int, col_idx: int) -> bool:
    col = [self.sudoku_map[row][col_idx] for row in range(9)]
    return num in col

  def block_checker(self, num: int, row_idx: int, col_idx: int) -> bool:
    start_row = (row_idx // 3) * 3
    start_col = (col_idx // 3) * 3

    for r in range(start_row, start_row + 3):
      for c in range(start_col, start_col + 3):
        if self.sudoku_map[r][c] == num:
          return True
    return False

  def is_valid(self, num: int, col_idx: int, row_idx: int) -> bool:
    return not (
        self.vertical_checker(num=num, col_idx=col_idx) or
        self.horizont_checker(num=num, row_idx=row_idx) or
        self.block_checker(num=num, row_idx=row_idx, col_idx=col_idx)
    )

  def hide_cells(self) -> None:
    col_pos = random.sample(range(81), 55)
    for i in range(0, 55):
      self.playable_sudoku_map[i % 9][col_pos[i] % 9] = 0